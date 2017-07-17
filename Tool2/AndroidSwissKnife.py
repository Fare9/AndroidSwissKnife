#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    File: AndroidSwissKnife.py
'''


'''
    Principal file, here we will parse user CLI  commands.
'''

import sys, signal, time, os, random, argparse, json
from Utilities.Help_vars import totalHelp
from Utilities.Useful_functions import  showTotalHelp
from Utilities.Useful_vars import banner
from Utilities.Useful_vars import bannerP
from Utilities.Useful_vars import verbosity
from Utilities.Useful_vars import apkInformation
from Core.File_checker import checkFile
from Core.ApktoolAnalysis import createApktoolFunc
from Core.UnzipAnalysis import unzipFunc
from Core.JadxAnalysis import jadxFunc

def main():

    parser = argparse.ArgumentParser(description="AndroidSwissKnife version 2.0 application to help in apk analysis")
    parser.add_argument("--install",action="store_true",help="To install some necessary tools")
    parser.add_argument("-a","--apk",type=str,help="apk file in your directory or absolute path")
    parser.add_argument("-o","--output",type=str,help="Name for output directories")
    parser.add_argument("--apktool",action="store_true",help="use apktool in Analysis")

    parser.add_argument("--unzip",action="store_true",help="use unzip in Analysis")
    parser.add_argument("--regEx",type=str,help='with unzip function we use a strings searching, you can add a regular Expression (by default URLs and Java Classes)')

    parser.add_argument("--jadx",action="store_true",help="use jadx to try to get source code")

    parser.add_argument("--all",action="store_true",help="use all Analysis")

    parser.add_argument("--exiftool",action="store_true",help="use exiftool with some file formats (you need first --apktool)")
    parser.add_argument("--man",action="store_true",help="Get all the help from the program as star wars film")
    parser.add_argument("--verbosity",type=int,help='Verbosity level (0 to 3)',default=1)
    parser.add_argument('--json',type=str,help="Get an output json file")
    args = parser.parse_args()

    if (args.verbosity is None) or (args.verbosity < 0) or (args.verbosity > 3):
        print("[-] Verbosity must be between 0 and 3")
        sys.exit(-1)

    verbosity = args.verbosity
    # first check if want to install

    # check if manual
    if args.man: # show all the help
        showTotalHelp()
        sys.exit(0)
    if args.apk is not None: # get apkfile
        apkFile = args.apk
    if args.output is not None: # get output file name
        outputName = args.output

    # for all
    allUse = args.all
    # for apktool
    apktoolUse = args.apktool
    exiftoolUse = args.exiftool
    # for unzip
    unzipUse = args.unzip
    regularExpression = args.regEx
    # for jadx
    jadxUse = args.jadx

    if (not allUse) and (not apktoolUse) and (not unzipUse) and (not jadxUse):
        print("[-] Use --help or -h to check help")
        sys.exit(0)
    
    # Check if user has given data
    if apkFile == '':
        print("[-] Use --help or -h to check help")
        sys.exit(0)
    if outputName == '':
        print("[-] Use --help or -h to check help")
        sys.exit(0)

    # check file for hashes
    checkFile(apkFile)
    input("Press enter to continue...")

    if allUse:
        createApktoolFunc(apkFile,outputName,exiftoolUse)
        unzipFunc(apkFile,outputName,regularExpression)
        jadxUse(apkFile,outputName)
    else: # Function by function
        if apktoolUse:
            createApktoolFunc(apkFile,outputName,exiftoolUse)
        if unzipUse:
            unzipFunc(apkFile,outputName,regularExpression)
        if jadxUse:
            jadxFunc(apkFile,outputName)
    # finally check if wants to write json file
    if args.json:
        with open(args.json, 'w') as outfile:
            json.dump(apkInformation, outfile)

if __name__ == '__main__':
    os.system('clear')
    print(random.choice(bannerP))
    time.sleep(1)
    os.system('clear')
    print (banner)
    time.sleep(1)
    os.system('clear')
    main()