#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: JadxAnalysis.py
'''


'''
    Functions for Jadx Analysis (at this moment just use jadx)
'''

import os,subprocess,sys
from Utilities.Print_functions import __print_verbosity
from Utilities.Print_functions import __print_list
from Utilities.Useful_vars import apkInformation

def jadxFunc(file,outputName):
    '''
    Get Java code with jadx, It is not the best way, but is the prettiest

    :param str file: input apk file to analyze
    :param str outputName: output name for jadx folder
    :return: None
    :rtype: None
    '''

    apkInformation['jadx'] = {}

    __print_verbosity(1,"[+] Creating directory from apk to jadx output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    # create name directory as: actualDirectory/jadx-outputName
    outputFile = actualDirectory + "/" + "jadx-" + outputName
    sentence = 'jadx ' + ' -d ' + outputFile + " " + file

    try:
        os.system(sentence)
        input("[!] Press enter")

        # show methods from files
        os.chdir(outputFile)
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.java'):
                    try:
                        __print_verbosity(0,'\t\t[+] SCANNING METHODS FROM: %s' % (os.path.join(root, file)))
                        methods = subprocess.check_output("cat %s | egrep %s" %(os.path.join(root, file),'"(public|protected|private) .+\(*\)"'),shell=True)
                        __print_list(0,methods.decode('utf-8').replace('{',''),'\n')
                        apkInformation['jadx'][os.path.join(root, file)] = methods.decode('utf-8').replace('{','').split('\n')
                    except Exception as e:
                        __print_verbosity(1,"Error: %s" % (str(e)))
                        continue
    except Exception as e:
        __print_verbosity(2,"[Debug] Error: %s" % (str(e)))
        __print_verbosity(1,"[-] Maybe you need jadx (try to use install function)...")

    os.chdir(actualDirectory)