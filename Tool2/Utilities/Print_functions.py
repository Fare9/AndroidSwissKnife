#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Utilities
    File: Print_functions.py
'''

'''
    Functions to manage print
'''

# verbosity we will check this variable in some functions
from Utilities.Useful_vars import verbosity




def __print_verbosity(verbosity_message,message):
    """
    Function to print a message depends of the verbosity

    :param int verbosity_message: verbosity of the message
    :param str message: message to show
    """

    if verbosity_message <= verbosity:
        print(message)

def __print_list(verbosity_message,message,separator):
    """
    Function to print a message with a tab first

    :param int verbosity_message: verbosity of the message
    :param str message: message to show
    """
    message = message.split(separator)
    if verbosity_message <= verbosity:
        for m in message:
            print("\t%s" % (m))
