#!/usr/bin/python

__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import argparse
import sys
import re

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

def process_args():
    """Process and parse the commandline arguments specified. 
    
    Returns:
       A dictionary with given arguments as keys. 
    """
    parser = argparse.ArgumentParser(description='Simpler Interface to send mail')
    parser.add_argument('--source', required=True, help='Source of email')
    parser.add_argument('--destination', required=True, help='Destination to email to')
    parser.add_argument('--subject', default='', help='Subject of the message.')
    parser.add_argument('--message', default='',  help='Main Body of the message.')
    parser.add_argument('--file', default='', help='Read specified text file and use that for the body of the message.') 
    parser.add_argument('--sendmail-binary', default='/usr/sbin/sendmail', help='Use specified copy of sendmail binary. Defaults to /usr/sbin/sendmail.')
    args = vars(parser.parse_args())
    
    # Quit if destination email is invalid.
    sanity_check_email(args['destination'])
    
    return args

def send_email(source, destination, subject, message, text_file=None)
    """Send an email using the send mail program. 

    Args:
        source: Source/Sender of the email.
        destination: Recipient of the email.
        subject: Subject/Title of the email.
        message: body content of the email
        text_file: if given, indicates that body of email should be read from text file.

    Returns:
        True upon success. 
    """
    

def main():
    process_args()

if __name__ == '__main__':
    main()

