#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: dex2jarAnalysis.py
'''

'''
    Use dex2jar to decompiling code
'''

import os
from Utilities.Print_functions import __print_verbosity

def getjarFunc(file):
    '''
    Function to call dex2jar, then you can see the code with others tools

    :param str file: apk file to analyze
    :return: None
    :rtype: None
    '''
    if not file:
        print("[-] Use --help or -h to check help")
        sys.exit(0)
        
    __print_verbosity(1,"[+] Creating Directory and jar from apk...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    nameNoAPK = file.replace('.apk', '')  # name without .apk
    nameDEX2JAR = nameNoAPK + '_dex2jar.jar'  # name from dex2jar output

    __print_verbosity(1,"[+] Creating file %s" % nameDEX2JAR)
    sentence = 'd2j-dex2jar ' + file
    os.system(sentence)

    __print_verbosity(1,"[+] Creating folder %s_CLASS and change directory" % nameNoAPK)
    print()
    os.mkdir('%s_CLASS' % nameNoAPK)
    os.chdir('%s_CLASS' % nameNoAPK)

    print("[+] Creating classes files")
    sentence = 'unzip ../' + nameDEX2JAR
    os.system(sentence)

    print("[+] Returning to: " + actualDirectory)
    os.chdir(actualDirectory)