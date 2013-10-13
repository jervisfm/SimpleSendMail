#!/usr/bin/python

__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import argparse
import os
import sys
import re

DEBUG = True

def quick_validate_email(email):
    """Does a basic check to ensure that email is a well-formed email address.

    Args:
       email: the address to check

    Returns:
        True if email is probably a conformant email address."""

    if not email:
        return False

    # Just follow the basic structure <some.thing>@<somet.hing>.<com>
    email_regex = "[a-zA-Z0-9_+\.]+@[a-zA-Z0-9.]+.[a-zA-Z0-9.]+"
    if re.search(email_regex, email): # email matches regex
        return True
    else:
        return False

def sanity_check_email(email):
    """If email determined to be invalid, informs user and quits."""
    if not quick_validate_email(email):
        print 'Invalid email entered: %s' % email
        print 'Please enter a valid email address and try again.'
        sys.exit(-1)

def sanity_check_emails(emails):
    if not emails:
        return False

    for email in emails:
        sanity_check_email(email)
    return True

def process_args():
    """Process and parse the commandline arguments specified. 
    
    Returns:
       A dictionary with given arguments as keys. 
    """

    help_epilog = ("Here is an example command:\n"
                      " python ssm.py --source=me@yahoo.com"
                      " --destination firstperson@gmail.com secondperson@gmail.com"
                      " --subject 'Hello' "
                      "--message 'Hello World'") 

    parser = argparse.ArgumentParser(description='Simpler Interface to send mail',epilog=help_epilog)
    parser.add_argument('--source', required=True, help='Source of email')
    parser.add_argument('--destination', nargs='+', required=True, help='Space separated list of destination email addresses to send email to.')
    parser.add_argument('--subject', default='', help='Subject of the message.')
    parser.add_argument('--message', default='',  help='Main Body of the message.')
    parser.add_argument('--file', default='', help='Read specified text file and use that for the body of the message.') 
    parser.add_argument('--sendmail-path', default='/usr/sbin/sendmail', help='User specified copy of sendmail binary. Defaults to /usr/sbin/sendmail.')
    args = vars(parser.parse_args())

    # Quit if source/destination email is invalid.
    sanity_check_emails(args['destination'] + [args['source']])
    
    if DEBUG:
        print args

    return args


def send_email(source, destination, subject, message, sendmail_path='/usr/sbin/sendmail', text_file=None):
    """Send an email using the send mail program. 

    Args:
        source: Source/Sender of the email.
        destination: A list of recipient(s) for the email.
        subject: Subject/Title of the email.
        message: body content of the email.
        sendmail_path: path of the send mail program to use. 
        text_file: if given, indicates that body of email should be read from text file.

    Returns:
        True upon success. 
    """
    # Check the Arguments
    if not source:
        raise ValueError("Source email must be provided")
    if not destination:
        raise ValueError("Destination email must be provided")

    if subject is None:
        subject = ''

    if text_file is not None:
        # Attempt to read the text_file and use it as the message. 
        try:
            with open(text_file, 'r') as f:
                content = f.read()
                message = content
        except IOError:
            if not message: # No message provided. Inform user and quit.
                print 'Error: Cannot read from file: %d and no --message parameter provided' % text_file
                print 'Please either specify a --message value or give a valid file'
                sys.exit(-1)
        
    # Construct the Message Body struct
    message_template = """\
From: %(source)s
To: %(destination)s
Subject: %(subject)s

%(body)s
"""
    message_dict = dict(source=source,
                        destination=', '.join(destination), # compile all emails addresses to comma separated list.
                        subject=subject,
                        body=message)
    email_message = message_template % message_dict

    if DEBUG:
        print 'Email Message Being Sent:%s\n' % email_message

    # Finally send the email
    sendmail_command = "%s -t -i" % sendmail_path
    process = os.popen(sendmail_command, "w")
    process.write(email_message)
    status = process.close()
    if status is not None: # Errors occurs
        print "Some errors occurred while sending email. Email has not been sent. Please try again later."
        return False
    else:
        print "Email Successfully Sent."
        return True

def main():
    args=process_args()

    # Send the email
    success = send_email(source=args['source'],
                         destination=args['destination'],
                         subject=args['subject'],
                         message=args['message'],
                         sendmail_path=args['sendmail_path'],
                         text_file=args['file'])
    if success:
        return 0
    else: # We failed.
        return -1

if __name__ == '__main__':
    main()
