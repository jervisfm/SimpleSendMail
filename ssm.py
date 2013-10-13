#!/usr/bin/python

__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import argparse
import sys

def process_args():
    """Process and parse the commandline arguments specified. 
    
    Returns:
       A dictionary with given arguments as keys. 
    """
    parser = argparse.ArgumentParser(description='Simpler Interface to send mail')
    parser.add_argument('--source', type=basestring, required=True, help='Source of email')
    parser.add_argument('--destination', type=basestring, required=True, help='Destination to email to')
    parser.add_argument('--subject', type=basestring, help='Subject of the message.')
    parser.add_argument('--message', type=basestring, help='Main Body of the message.')
    parser.add_argument('--file', type=basestring, help='Read specified text file and use that for the body of the message.') 
    args = vars(parser.parse_args())
    return args


def main():
    process_args()


if __name__ == '__main__':
    main()

