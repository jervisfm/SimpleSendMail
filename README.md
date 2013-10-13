
Author: Jervis Muindi
Date: October 2013

Introduction
============
This is a simple python program that aims to provide a simpler interface to sendmail
for sending textual emails. 

It is primarily designed to run on UNIX system that have the sendmail utility installed. 

The primary motivation came from find the sendmail interface too arcane to send a simple email. 
I felt overwhelemd by the sheer number of options which are exposed to the user. This script hides
all that complexity and presents a simple interface. 


Dependency
==========
###Argparse:
This is used to do argument processing so the argparse module should be install. This
module should be standard on Python 2.7 and later.

If you are on an older version of python, you can still install argparse through the PIP Python
Package manager. From your terminal execute:

$ pip install argparse

How to Run
===========
Details on running the program are described below: 

<pre>
usage: ssm.py [-h] --source SOURCE --destination DESTINATION [DESTINATION ...]
              [--subject SUBJECT] [--message MESSAGE] [--file FILE]
              [--sendmail-binary SENDMAIL_BINARY]

Simpler Interface to send mail

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       Source of email
  --destination DESTINATION [DESTINATION ...]
                        Space separated list of destination email addresses to
                        send email to.
  --subject SUBJECT     Subject of the message.
  --message MESSAGE     Main Body of the message.
  --file FILE           Read specified text file and use that for the body of
                        the message.
  --sendmail-binary SENDMAIL_BINARY
                        Use specified copy of sendmail binary. Defaults to
                        /usr/sbin/sendmail.

Here is an example command: python ssm.py --source=me@yahho.com --destination
firstperson@gmail.com secondperson@gmail.com --subject 'Hello' --message
'Hello World'
</pre>