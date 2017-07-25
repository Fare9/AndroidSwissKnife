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

try:
    import sys, signal, time, os, random, argparse, json, pprint
    from Utilities.Help_vars import totalHelp
    from Utilities.Useful_functions import  showTotalHelp
    from Utilities.Useful_vars import banner
    from Utilities.Useful_vars import bannerP
    from Utilities.Useful_vars import verbosity
    from Utilities.Useful_vars import apkInformation
    from Core.File_checker import checkFile
    from Core.ApktoolAnalysis import createApktoolFunc
    from Core.ApktoolAnalysis import createAPKFunc
    from Core.UnzipAnalysis import unzipFunc
    from Core.JadxAnalysis import jadxFunc
    from Core.OpcodeAnalysis import opcodesFunc
    from Core.dex2jarAnalysis import getjarFunc
    from Core.Koodous import KoodousAnalyzer
    from Core.DynamicAnalyzer import DroidBox
    from Core.Installer import install
except:
    import sys, signal, time, os, random, argparse, json, pprint
    from Core.Installer import install
    
def check_cli(args):

    if (args.verbosity is None) or (args.verbosity < 0) or (args.verbosity > 3):
        print("[-] Verbosity must be between 0 and 3")
        sys.exit(-1)

    verbosity = args.verbosity
    # first check if want to install
    if args.install:
        install()
    # check if manual
    if args.man: # show all the help
        showTotalHelp()
        sys.exit(0)
    

    apkFile = args.apk
    outputName = args.output


    if (not args.all) and (not args.apktool) and (not args.unzip) and (not args.jadx) and (not args.opcodes) and (
        not args.get_jar) and (not args.create_apk) and (not args.Koodous) and (not args.DroidBox):
        print("[-] Use --help or -h to check help")
        sys.exit(0)
    

    # check if user wants koodous report
    if args.Koodous:
        koodous = KoodousAnalyzer(apk=apkFile,upload=args.upload)
        koodous.analyzeApk()
        pprint.pprint(koodous.jsonOutput, indent=4)
        with open('koodous.json', 'w') as outfile:
            print("[+] Creating koodous.json file")
            json.dump(koodous.jsonOutput, outfile)

    # check if user wants to create apk from folder
    if args.create_apk:
        createAPKFunc(args.folder,args.apk_output)


    # check file for hashes
    checkFile(apkFile)
    input("Press enter to continue...")

    if args.all:
        createApktoolFunc(apkFile,outputName,args.exiftool)
        unzipFunc(apkFile,outputName,args.regEx)
        jadxFunc(apkFile,outputName)
        opcodesFunc(apkFile,outputName)
        getjarFunc(apkFile)
    else: # Function by function
        if args.apktool:
            createApktoolFunc(apkFile,outputName,args.exiftool)
        if args.unzip:
            unzipFunc(apkFile,outputName,args.regEx)
        if args.jadx:
            jadxFunc(apkFile,outputName)
        if args.opcodes:
            opcodesFunc(apkFile,outputName)
        if args.get_jar:
            getjarFunc(apkFile)

    # check if user wants dynamic analysis
    if args.DroidBox:
        droidbox = DroidBox(apkFile,args.Device,args.Burp)
        droidbox.run()

    # finally check if wants to write json file
    if args.json:
        with open(args.json, 'w') as outfile:
            json.dump(apkInformation, outfile)

def main():

    parser = argparse.ArgumentParser(description="AndroidSwissKnife version 2.0 application to help in apk analysis")
    parser.add_argument("--install",action="store_true",help="To install some necessary tools")
    parser.add_argument("-a","--apk",type=str,help="apk file in your directory or absolute path")
    parser.add_argument("-o","--output",type=str,help="Name for output directories")
    parser.add_argument("--apktool",action="store_true",help="use apktool in Analysis")

    parser.add_argument("--unzip",action="store_true",help="use unzip in Analysis")
    parser.add_argument("--regEx",type=str,help='with unzip function we use a strings searching, you can add a regular Expression (by default URLs and Java Classes)')

    parser.add_argument("--jadx",action="store_true",help="use jadx to try to get source code")

    parser.add_argument("--opcodes",action="store_true",help="Get information from opcodes")

    parser.add_argument("--get-jar",action="store_true",help="Get jar from apk and finally the .class in a folder")


    parser.add_argument("--create-apk",action="store_true",help="generate an apk, from apktool folder use -f <folder> --apk-output <output.apk>")
    parser.add_argument("-f","--folder",type=str,help='folder from apktool (needs --create-apk)')
    parser.add_argument("--apk-output",type=str,help='Output apk (needs --create-apk)')


    parser.add_argument("--Koodous",action="store_true",help="Try to search your apk in Koodous, it will take some time")
    parser.add_argument("--upload",action="store_true",help="If APK is not in koodous upload to analysis")


    parser.add_argument('--DroidBox',action='store_true',help='Dynamic Analysis with DroidBox (Android 4.2)')
    parser.add_argument('--Device',type=str,help='Device Name to start')
    parser.add_argument('--Burp',action='store_true',help='Start Burp to use proxy analysis')

    parser.add_argument("--all",action="store_true",help="use all Analysis")

    parser.add_argument("--exiftool",action="store_true",help="use exiftool with some file formats (you need first --apktool)")
    parser.add_argument("--man",action="store_true",help="Get all the help from the program as star wars film")
    parser.add_argument("--verbosity",type=int,help='Verbosity level (0 to 3)',default=1)
    parser.add_argument('--json',type=str,help="Get an output json file")
    args = parser.parse_args()

    check_cli(args)


if __name__ == '__main__':
    os.system('clear')
    print(random.choice(bannerP))
    time.sleep(1)
    os.system('clear')
    print (banner)
    time.sleep(1)
    os.system('clear')
    main()