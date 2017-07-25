#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: ApktoolAnalysis.py
'''

'''
    Functions for analysis with apktool, also we have function
    to create apk from apktool folder output
'''

'''
    Classes that will help with android dynamic analysis
    we will use adb to start an emulator, install apk, run
    and also use proxy

    Why another class file with classes? If you create a 
    complex structure nobody can understand it.

    A sentence which can explain about this class:

    "Ja hem traçat un llarg camí fins aquí, 
    I tots nosaltres portem dins dels nostres cors, 
    promeses que no podem deixar enrere" 
                                    Miree

    Original DroidBox Idea: 
        Patrik Lantz patrik@pjlantz.com and Laurent Delosieres ldelosieres@hispasec.com
        The Honeynet Project

    I modified some parts from code and I use another methods for example to parse XML
    and I have adapted to my code. My ideas added to Program:

        - Start Burpsuite (I'm not owner from Burpsuite, https://portswigger.net/burp/)
        - No need startmenu.sh, gnome-terminal will open emulator in another window
        - Use of apktool to unzip  apk
        - Use of BeautifulSoup to parse XML

    Any suggestion please contact me in farenain9@gmail.com
'''


import os,sys,sqlite3,pprint
import exiftool
import subprocess # for call 
import time
from threading import Thread
from bs4 import BeautifulSoup
from IPy import IP

from Utilities.Useful_functions import getHashes
from Utilities.Useful_functions import find
from Core.adbClass import ThreadAnalyzer,Proxy,Adb,getTags


from Utilities.Print_functions import __print_verbosity
from Utilities.Useful_vars import apkInformation
from Utilities.Useful_vars import WARNING
from Utilities.Useful_vars import FAIL
from Utilities.Useful_vars import ENDC
from Utilities.Useful_functions import parseObjDump
from Libs.permissions import normal_things,strange_things,problem_things
from Libs.filters import filterString


def createApktoolFunc(file, outputName, exiftoolUse):
    '''
    Module to get directory with apk resolution from apktool, well we need apktool. 

    :param str file: input apk file
    :param str outputName: output name for apktool folder
    :param bool exiftoolUse: boolean to check if we will use exiftool or not
    :return: None
    :rtype: None
    '''

    if not file or not outputName:
        print("[-] Use --help or -h to check help")
        sys.exit(0)

    __print_verbosity(1,"[+] Creating Directory from apk to apktool output...")

    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    # create name directory as: actualDirectory/apktool-outputName
    outputFile = actualDirectory + "/" + "apktool-" + outputName
    sentence = 'apktool d ' + file + ' -o ' + outputFile

    __print_verbosity(1,"[+] Directory output name: %s" % (outputFile))
    try:
        os.system(sentence)
        input("[!] Press enter")
        __readAndroidManifest(outputFile)
        input("[!] Press enter")
        __readInterestingFilters(outputFile)
        input("[!] Press enter")
        __readLibraries(outputFile)
        input("[!] Press enter")

        if exiftoolUse:
            __extractMetaData(outputFile)
            input("[!] Press enter")

        __readDatabases(outputFile)
        input("[!] Press enter")

        static_analysis = StaticComleteAnalysis(file,outputFile)
    except Exception as e:
        os.chdir(actualDirectory)
        __print_verbosity(2,"[-] ERROR createApktoolFunc %s" % (str(e)))
        __print_verbosity(1,"[-] Maybe you need apktool...")


def __readAndroidManifest(directory):
    '''
    Module to read AndroidManifest we will add some features from static analysis
    Please add what you want if you thing something is strange

    :param str directory: directory where createApktoolFunc has created its output
    :return: None
    :rtype: None
    '''
    apkInformation['permissions'] = {}

    actualDirectory = os.getcwd()  # to return after analysis of AndroidManifest

    # change to apktool directory and read AndroidManifest.xml
    __print_verbosity(1,'[+] Change directory to: %s' % (directory))
    os.chdir(directory)

    amFile = open('AndroidManifest.xml', 'rb')
    xmlString = str(amFile.read())

    # show in terminal
    __print_verbosity(0,'[+] Printing AndroidManifest.xml')
    __print_verbosity(0,xmlString.replace('\\n', '\n'))

    # Let's go with static analysis
    __print_verbosity(1,'[!] Maybe normal things...')
    apkInformation['permissions']['Normal_Things'] = []
    for key in normal_things:
        if key in xmlString:
            apkInformation['permissions']['Normal_Things'].append(key)
            __print_verbosity(0,normal_things[key])

    __print_verbosity(0,"%s" % WARNING)
    __print_verbosity(1,'[!] Maybe some strange things...')
    apkInformation['permissions']['Strange_Things'] = []
    for key in strange_things:
        if key in xmlString:
            apkInformation['permissions']['Strange_Things'].append(key)
            __print_verbosity(0,strange_things[key])
    __print_verbosity(0,"%s" % ENDC)

    __print_verbosity(0,"%s" % FAIL)
    __print_verbosity(1,'[!] Ohh so strange things...')
    apkInformation['permissions']['Problem_Things'] = []
    for key in problem_things:
        if key in xmlString:
            apkInformation['permissions']['Problem_Things'].append(key)
            __print_verbosity(0,problem_things[key])
    __print_verbosity(0,"%s" % ENDC)

    # close file
    amFile.close()
    # finally we return to directory
    __print_verbosity(1,'[+] Change directory to: %s' % (actualDirectory))
    os.chdir(actualDirectory)


def __readInterestingFilters(directory):
    '''
    Module to read the manifest file and show interesting filters

    :param str directory: output directory from createApktoolFunc
    :return: None
    :rtype: None
    '''
    apkInformation['Filters'] = []


    actualDirectory = os.getcwd()  # to return after analysis of AndroidManifest

    # change to apktool directory and read AndroidManifest.xml
    __print_verbosity(1,'[+] Change directory to: %s' % (directory))
    os.chdir(directory)

    amFile = open('AndroidManifest.xml', 'rb')
    xmlString = str(amFile.read())
    __print_verbosity(0,"[+] Let's going to look for interesting filters")

    __print_verbosity(1,'[+] Stranger filters: ')
    print()
    for key in filterString:
        if key in xmlString:
            apkInformation['Filters'].append(key)
            __print_verbosity(0,filterString[key])

    # close file
    amFile.close()
    # finally we return to directory
    __print_verbosity(1,'[+] Change directory to: ' + actualDirectory)
    os.chdir(actualDirectory)


def __readLibraries(directory):
    '''
    Process to read library from android native libraries, discover Java functions and finally dissassembling it
    This extract Native code(arm,intel or mips).

    :param str directory: output directory from createApktoolFunc
    :return: None
    :rtype: None
    '''
    apkInformation['Native_Methods'] = []


    actualDirectory = os.getcwd()

    __print_verbosity(1,'[+] Change directory to: %s' % (directory))
    os.chdir(directory)

    __print_verbosity(0,'[+] Listing all native libraries')
    __print_verbosity(1,'[+] It will show java class from those libraries')

    for root, dirs, files in os.walk('.'):
        for file in files:
            try:
                if file.endswith('.so'):  # If it is .so file (native library)
                    pathFile = os.path.join(root, file)
                    __print_verbosity(0,WARNING)
                    __print_verbosity(0,"[+] File: %s" % (pathFile))
                    __print_verbosity(0,ENDC)
                    statement = 'objdump -T ' + pathFile + ' | grep Java_'  # we use objdump to show strings then find Java functions
                    # os.system(statement)
                    error = False
                    try:
                        output = subprocess.check_output(statement, shell=True)
                    except subprocess.CalledProcessError as e:
                        __print_verbosity(1,"[-] Error in objdump: %s" % (str(e)))
                        error = True

                    if error:
                        __print_verbosity(2,output)
                    else:
                        native_methods = parseObjDump(output,pathFile)
                        pprint.pprint(native_methods)
                        apkInformation['Native_Methods'].append(native_methods)

                    print("[+] Disassembling file in: " + file + ".txt")
                    if "arm" in pathFile:  # for arm libs
                        statement = 'arm-linux-androideabi-objdump -d ' + pathFile + ' > ' + file + '.txt'
                        os.system(statement)
                    elif "86" in pathFile:  # for x86 32 bits libs
                        statement = 'i686-linux-android-objdump -d ' + pathFile + ' > ' + file + '.txt'
                        os.system(statement)
                    elif "mips" in pathFile:  # just for Rico's mind
                        statement = 'mipsel-linux-android-objdump -d ' + pathFile + ' > ' + file + '.txt'
                        os.system(statement)
                        # end if
            except: #maybe not Java functions
                continue
    __print_verbosity(1,'[+] Returning to directory: %s' % (actualDirectory))
    os.chdir(actualDirectory)


def __readDatabases(directory):
    '''
    Extract schema from SQLite Database

    :param str directory: output directory from createApktoolFunc
    :return: None
    :rtype: None
    '''
    actualDirectory = os.getcwd()

    apkInformation['Databases'] = []
    jsonToAppend = {} # to append in apkInformation

    __print_verbosity(0,'[+] Let\'s going to read databases')
    __print_verbosity(1,'[+] Change directory to: %s' % (directory))
    os.chdir(directory)

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.db') or file.endswith('.sqlite'):
                pathFile = os.path.join(root, file)

                __print_verbosity(0,"[!] DataBase: %s" % (pathFile))

                jsonToAppend['Database'] = ''
                jsonToAppend['Database'] = pathFile

                # create connection and execute sqlite queries
                con = sqlite3.connect(pathFile)
                cursor = con.cursor()
                tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                for table in tables:
                    __print_verbosity(0,"\t[+] Table: %s" % (table[0]))

                    jsonToAppend['Table'] = ''
                    jsonToAppend['Table'] = table[0]

                    columns = cursor.execute("SELECT * FROM %s;"%(table[0])).description

                    jsonToAppend['Columns'] = []

                    for column in columns:

                        jsonToAppend['Columns'].append(column[0])

                        __print_verbosity(0,"\t\t[+] Column: %s" % (column[0]))

                    # Insert into JSON Output
                    apkInformation['Databases'].append(jsonToAppend)

    __print_verbosity(1,'[+] Returning to directory: %s' % (actualDirectory))
    os.chdir(actualDirectory)


def __extractMetaData(directory):
    '''
        Program to extract metadata from files .jpg,.png,.pdf,.csv,.txt...

    :param str directory: output directory from createApktoolFunc
    :return: None
    :rtype: None
    '''
    jpgFormat = False
    pngFormat = False
    pdfFormat = False
    csvFormat = False
    txtFormat = False
    xmlFormat = False

    actualDirectory = os.getcwd()

    apkInformation['Metadata'] = {}

    __print_verbosity(1,'[+] Change diretory to: %s' % (directory))
    os.chdir(directory)

    __print_verbosity(0,'[+] Now you will select files to extract metadata, \'y\' to select that extension, another one to refuse')

    if str(input('\t[+] JPG: ')).lower() == 'y':
        jpgFormat = True

    if str(input('\t[+] PNG: ')).lower() == 'y':
        pngFormat = True

    if str(input('\t[+] PDF: ')).lower() == 'y':
        pdfFormat = True

    if str(input('\t[+] CSV: ')).lower() == 'y':
        csvFormat = True

    if str(input('\t[+] TXT: ')).lower() == 'y':
        txtFormat = True

    if str(input('\t[+] XML: ')).lower() == 'y':
        xmlFormat = True

    try:
        with exiftool.ExifTool as et:
            if jpgFormat:
                apkInformation['Metadata']['JPG'] = []
                for root, dirs, files in os.walk('.'):
                    for file in files:
                        if file.endswith('.jpg'):
                            __print_verbosity(0,"[+] Showing metadata for: %s" % (os.path.join(root, file)))
                            metadata = et.get_metadata(os.path.join(root, file))
                            pprint.pprint(metadata)
                            apkInformation.append({os.path.join(root, file):metadata})
                            time.sleep(0.5)

            if pngFormat:
                apkInformation['Metadata']['PNG'] = []
                for root, dirs, files in os.walk('.'):
                    for file in files:
                        if file.endswith('.png'):
                            __print_verbosity(0,"[+] Showing metadata for: %s" % (os.path.join(root, file)))
                            metadata = et.get_metadata(os.path.join(root, file))
                            pprint.pprint(metadata)
                            apkInformation.append({os.path.join(root, file):metadata})
                            time.sleep(0.5)

            if pdfFormat:
                apkInformation['Metadata']['PDF'] = []
                for root, dirs, files in os.walk('.'):
                    for file in files:
                        if file.endswith('.pdf'):
                            __print_verbosity(0,"[+] Showing metadata for: %s" % (os.path.join(root, file)))
                            metadata = et.get_metadata(os.path.join(root, file))
                            pprint.pprint(metadata)
                            apkInformation.append({os.path.join(root, file):metadata})
                            time.sleep(0.5)

            if csvFormat:
                apkInformation['Metadata']['CSV'] = []
                for root, dirs, files in os.walk('.'):
                    for file in files:
                        if file.endswith('.csv'):
                            __print_verbosity(0,"[+] Showing metadata for: %s" % (os.path.join(root, file)))
                            metadata = et.get_metadata(os.path.join(root, file))
                            pprint.pprint(metadata)
                            apkInformation.append({os.path.join(root, file):metadata})
                            time.sleep(0.5)

            if txtFormat:
                apkInformation['Metadata']['TXT'] = []
                for root, dirs, files in os.walk('.'):
                    for file in files:
                        if file.endswith('.txt'):
                            __print_verbosity(0,"[+] Showing metadata for: %s" % (os.path.join(root, file)))
                            metadata = et.get_metadata(os.path.join(root, file))
                            pprint.pprint(metadata)
                            apkInformation.append({os.path.join(root, file):metadata})
                            time.sleep(0.5)

            if xmlFormat:
                apkInformation['Metadata']['XML'] = []
                for root, dirs, files in os.walk('.'):
                    for file in files:
                        if file.endswith('.xml'):
                            __print_verbosity(0,"[+] Showing metadata for: %s" % (os.path.join(root, file)))
                            metadata = et.get_metadata(os.path.join(root, file))
                            pprint.pprint(metadata)
                            apkInformation.append({os.path.join(root, file):metadata})
                            time.sleep(0.5)

    except Exception as e:
        __print_verbosity(2,"Error: %s" % (str(e)))
        print('[-] Error, maybe you need exiftool')
    finally:
        print('[+] Returning to: ' + actualDirectory)
        os.chdir(actualDirectory)


def createAPKFunc(folder, apkName):
    '''
    If you change smali code from apktool output, you can pack again in apk file with this function

    :param str folder: output folder from apktool to convert to apk
    :param str apkName: output apk name
    :return: None
    :rtype: None
    '''
    if not folder or apkName:
        print("[-] Use --help or -h to check help")
        sys.exit(0)

    print('[+] Creating temporary file before sign apk')
    sentence = 'apktool b ' + folder + ' -o changed_apk.apk'
    os.system(sentence)

    files = os.listdir('.')

    if 'changed_apk.apk' in files:
        __print_verbosity(0,'[+] Creating signed apk')
        sentence = 'd2j-apk-sign -f -o ' + apkName + ' changed_apk.apk'
        os.system(sentence)
        __print_verbosity(0,'[+] Removing temporary file')
        os.remove('changed_apk.apk')
        __print_verbosity('[+] Well now you can use your new apk')
    else:
        print('[-] There was a problem with apktool and temporary file')


class StaticComleteAnalysis():
    """
    Class taken from DroidBox for Dynamic Analysis
    I will change some functions which I think I can
    do in another way
    """
    def __init__(self,apk,outputFile):
        '''
        Constructor of the class

        :param str apk: path to apk to analyze
        :return: None
        :rtype: None
        '''
        self.apk = apk
        self.outputFile = outputFile
        self.packages = []
        self.permissions = []
        self.outPermissions = [] #this permissions are for others apps
        self.receivers = []
        self.recvsactions = {}
        self.activities = {}
        

        self.mainActivity = None

    def showInfo(self):
        '''
        Method to show and save info in json

        :return: None
        :rtype: None
        '''
        apkInformation['static_analysis'] = {}


        print('[+] APK: %s' % self.apk)
        apkInformation['static_analysis']['apk'] = self.apk

        print('[+] Packages: ')
        pprint.pprint(self.packages)
        apkInformation['static_analysis']['packages'] = self.packages

        print('[+] Permissions: ')
        pprint.pprint(self.permissions)
        apkInformation['static_analysis']['permissions'] = self.permissions

        print('[+] Out Permissions (permissions for other apps): ')
        pprint.pprint(self.outPermissions)
        apkInformation['static_analysis']['out_permissions'] = self.outPermissions

        print('[+] Receivers: ')
        pprint.pprint(self.receivers)
        apkInformation['static_analysis']['receivers'] = self.receivers

        print('[+] Receivers actions: ')
        pprint.pprint(self.recvsactions)
        apkInformation['static_analysis']['recvsactions'] = self.recvsactions

        print('[+] Activities: ')
        pprint.pprint(self.activities)
        apkInformation['static_analysis']['activities'] = self.activities

        print('[+] Main Activity: %s' % self.mainActivity)
        apkInformation['static_analysis']['mainActivity'] = self.mainActivity


    def extractingApkInfo(self):
        """
        Extract information from apk, I will use BeautifulSoup instead of
        XML libraries

        :return: None
        :rtype: None
        """
        try:
            manifest = None
            
            if not self.outputFile: # if not executed by apktoolanalysis
                apkName = self.apk
                apkName = os.path.basename(apkName)
                apkName = apkName.replace(".apk","")
                unzipFolder = "apktool-"+apkName
                actualDirectory = os.getcwd()
                outputFile = actualDirectory + "/" + "apktool-" + apkName
                sentence = 'apktool d '+self.apk+' -o '+outputFile
                print("[+] Unzipping apk")
                subprocess.call(sentence,shell=True)
                manifest = open(unzipFolder+"/AndroidManifest.xml","rb")
            else:
                manifest = open(self.outputFile+"/AndroidManifest.xml",'rb')
            
            bsObj = BeautifulSoup(manifest.read(),'html.parser')

            ## Now start parsing

            # package
            packages= bsObj.findAll("manifest")
            for package in packages:
                self.packages.append(str(package['package']))

            #print("[+] Packages: "+str(self.packages))
            # uses-permission
            usespermissions = bsObj.findAll("uses-permission")
            for usespermission in usespermissions:
                self.permissions.append(str(usespermission['android:name']))

            #print('[+] Uses-Permissions: '+str(self.permissions))
            # out permissions
            permissions = bsObj.findAll("permission")
            for permission in permissions:
                self.outPermissions.append(str(permission['android:name']))
            #print('[+] Permissions: '+str(self.outPermissions))
            #  Receivers and actions from that receiver
            ##  1 Receiver can have 0 or more actions, then actions should be a list
            receivers = bsObj.findAll("receiver")
            for receiver in receivers:
                self.receivers.append(receiver['android:name'])
                actions = receiver.findAll("action")
                self.recvsactions[receiver['android:name']] = list()
                for action in actions:
                    self.recvsactions[receiver['android:name']].append(action['android:name'])

            #print("[+] Receivers: "+str(self.receivers))
            #print("[+] RecvsActions: "+str(self.recvsactions))
            # Now activities, activities can have actions and categories
            activities = bsObj.findAll("activity")
            for activity in activities:
                # let's take actions and categories
                self.activities[activity['android:name']] = {}
                self.activities[activity['android:name']]["actions"] = list()
                actions = activity.findAll("action")
                for action in actions:
                    self.activities[activity['android:name']]["actions"].append(action['android:name'])

                self.activities[activity['android:name']]["categories"] = list()
                categories = activity.findAll('category')
                for category in categories:
                    self.activities[activity['android:name']]["categories"].append(category['android:name'])
            #print("[+] Activities: "+str(self.activities))
            # well extract which is the main activity
            for activity in self.activities:
                if "android.intent.action.MAIN" in self.activities[activity]["actions"]:
                    self.mainActivity = activity 
                    break
            #print("[+] MainActivity: "+str(self.mainActivity))

        except Exception as e:
            __print_verbosity(2,"[+] Error parsing AndroidManifest: %s" % str(e))