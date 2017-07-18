#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: OpcodeAnalysis.py
'''


'''
    Analysis of assembly opcodes from operating system depend code
'''

import xml.etree.ElementTree as ET
import subprocess  # for data from files
import os,sys

from Utilities.Useful_vars import apkInformation
from Utilities.Print_functions import __print_verbosity


def opcodesFunc(file,outputName):
    '''

    :param str file: input apk file
    :param str outputName: output name for apktool folder
    :return: None
    :rtype: None
    '''
    __getOpcodes(file,outputName)
    __receiversOpcodes(file)



def __getOpcodes(file, outputName):
    '''

    :param str file: input apk file
    :param str outputName: output name for apktool folder
    :return: None
    :rtype: None
    '''


    __print_verbosity(1,"[+] Creating files from apk to dexdump output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    __print_verbosity(0,'[+] Creating opcodes file...')
    outputFile = actualDirectory + "/" + "opcode-" + outputName + ".txt"
    sentence = 'dexdump ' + ' -d ' + file + ' > ' + outputFile

    try:
        subprocess.call(sentence,shell=True)
        input("[!] Press enter")
    except Exception as e:
        __print_verbosity(2,"[Debug] Error: %s" % str(e))
        __print_verbosity(1,"[-] Maybe you need dexdump...")

    __print_verbosity(0,'[+] Creating headers file...')
    outputFile = actualDirectory + "/" + "summary-" + outputName + ".txt"
    sentence = 'dexdump ' + ' -f ' + file + ' > ' + outputFile

    try:
        subprocess.call(sentence,shell=True)
        input("[!] Press enter")
    except Exception as e:
        __print_verbosity(2,"[Debug] Error: %s" % str(e))
        __print_verbosity(1,"[-] Maybe you need dexdump...")

    __print_verbosity(0,'[+] Creating aditional informations about headers file...')
    outputFile = actualDirectory + "/" + "summaryDetails-" + outputName + ".txt"
    sentence = 'dexdump ' + ' -f ' + file + ' > ' + outputFile

    try:
        subprocess.call(sentence,shell=True)
        input("[!] Press enter")
    except Exception as e:
        __print_verbosity(2,"[Debug] Error: %s" % str(e))
        __print_verbosity(1,"[-] Maybe you need dexdump...")


    

def __receiversOpcodes(file):
    '''
    Get Receivers from opcodes and receivers in AndroidManifest

    :param str file: apk file to analyze
    :return: None
    :rtype: None
    '''

    apkInformation['receivers'] = {}
    #### Now get receiver from androidManifest and Code
    # First from code
    ReceiverCode = list()

    command = "dexdump -i -l xml " + file
    output = subprocess.check_output(command, shell=True)
    xml = ET.fromstring(output)

    for node in xml.iter("class"):  # iterate from all xml tree
        # Look for BroadcastReceiver
        if node.attrib["extends"] == "android.content.BroadcastReceiver":
            package = ""
            for child in node.iter("constructor"):
                package = child.attrib["type"]
            # for every BroadcastReceiver put into the list
            ReceiverCode.append(package + "." + node.attrib["name"])

    ReceiverAndroidManifest = list()
    # Create "AndroidManifest.xml file"
    outputManifestFile = "/tmp/AndroidManifest.xml.tmp"

    __print_verbosity(1,"[+] Using manifestDecoder")
    # Fixed problems to use with python3
    command = "Libs/manifestDecoder.py " + file
    os.system(command)

    command = "cat " + outputManifestFile + " | grep manifest | sed -nE 's/.*package=\"([^\"]+)\".*/\\1/p'"
    package = subprocess.check_output(command, shell=True)  # .replace("\n", "")
    package = str(package).replace("\n", "")

    command = "cat " + outputManifestFile + " | grep " + "receiver" + " | sed -nE 's/.*" + "name" + "=\"([^\"]+)\".*/\\1/p'"
    elements = subprocess.check_output(command, shell=True)
    elements = str(elements).split("\n")
    for element in elements:
        if element and element.strip():
            if (element.startswith(".")):
                ReceiverAndroidManifest.append(package + element)
            else:
                ReceiverAndroidManifest.append(element)

    os.remove(outputManifestFile)

    __print_verbosity(0,'[+] Receivers in code from hexdump: ')
    for rc in ReceiverCode:
        __print_verbosity(0,'\t[+] %s' % rc)

    __print_verbosity(0,'[+] Receivers in AndroidManifest: ')
    for ra in ReceiverAndroidManifest:
        __print_verbosity(0,'\t[+] %s' % ra)

    __print_verbosity(0,'[+] Receivers that are in code but not in AndroidManifest: ')
    for rc in ReceiverCode:
        found = False
        for ra in ReceiverAndroidManifest:
            if (rc.startswith(ra)):
                found = True
                break
        if not found:
            __print_verbosity(0,'\t[+] %s' % rc)

    apkInformation['receivers']['code'] = ReceiverCode
    apkInformation['receivers']['manifest'] = ReceiverAndroidManifest 