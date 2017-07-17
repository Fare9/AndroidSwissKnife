#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: ApktoolAnalysis.py
'''

'''
    Useful functions to use in the program
'''

import signal,sys,time, hashlib
from Utilities.Help_vars import totalHelp


def parseObjDump(text,file_):
    '''
    I will parse output of objdump, something like this:
    0000dd75 g    DF .text  00000026 Java_com_Titanium_Magister_sursumApp_nativesursumAppCall

    We will call this method from readLibraries in androidSwissKnife.py

    :param str text: function output from objdump
    :param str file_: path to operating system file
    :return: dictionary with file and methods
    :rtype: dict
    '''
    output = []
    lines = text.split(b'\n')
    for line in lines:
        if len(line) < 1:
            continue
        dictionary = {}
        line = str(line)
        line = line.strip()
        line = line.replace('\\t',' ')

        strippedLine = line.split()

        dictionary['symbol_value'] = strippedLine[0]
        dictionary['symbols'] = strippedLine[1]
        if dictionary['symbols'] == 'l':
            dictionary['kind_symbol'] = 'local'

        elif dictionary['symbols'] == 'g':
            dictionary['kind_symbol'] = 'global'

        elif dictionary['symbols'] == 'u':
            dictionary['kind_symbol'] = 'unique global'

        elif dictionary['symbols'] == '!':
            dictionary['kind_symbol'] = 'both or neither (global/local)'

        elif dictionary['symbols'] == 'w':
            dictionary['kind_symbol'] = 'weak or strong symbol'

        elif dictionary['symbols'] == 'C':
            dictionary['kind_symbol'] = 'Constructor'

        elif dictionary['symbols'] == 'W':
            dictionary['kind_symbol'] = 'Warning'

        elif dictionary['symbols'] == 'd':
            dictionary['kind_symbol'] = 'Debugging symbol'

        elif dictionary['symbols'] == 'D':
            dictionary['kind_symbol'] = 'Dynamic symbol'

        elif dictionary['symbols'] == 'F':
            dictionary['kind_symbol'] = 'Symbol is a Function name'

        elif dictionary['symbols'] == 'f':
            dictionary['kind_symbol'] = 'Symbol is a File name'
        
        elif dictionary['symbols'] == 'O':
            dictionary['kind_symbol'] = 'Symbol is a Object name'

        #print(dictionary['kind_symbol'])
        dictionary['section'] = strippedLine[3]
        #print(dictionary['section'])
        dictionary['size'] = strippedLine[4]
        #print(dictionary['size'])
        dictionary['method'] = strippedLine[5]
        #print(dictionary['method'])

        output.append(dictionary)

    return {"File":file_,"Methods":output}


def handler(signum, frame):
    '''
    Method to show total help if user press CTRL-C

    :param int signum: Signal Number
    :param int frame: Signal frame
    :return: None
    :rtype: None
    '''
    print("Ohh don't like help print?")
    print (totalHelp)
    sys.exit(0)


def showTotalHelp():
    '''
    Module to show all the help
    '''
    signal.signal(signal.SIGINT, handler)
    print("Press CTRL-C to skip")
    for c in totalHelp:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.05)


def getHashes(apkFile):
    '''
    Method to get md5, sha1 and sha256 from an apk

    :param str apkFile: path to apk file
    :return: md5,sha1 and sha256 hashes
    :rtype: list
    '''
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    f = open(apkFile,'rb')

    #now we read the apk and create hashes
    while True:
        data = f.read(512)
        if not data:
            break

        md5.update(data)
        sha1.update(data)
        sha256.update(data)

    return [md5.hexdigest(),sha1.hexdigest(),sha256.hexdigest()]
