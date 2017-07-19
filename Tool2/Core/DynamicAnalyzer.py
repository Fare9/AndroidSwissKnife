#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: DynamicAnalyzer.py
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

import subprocess # for call 
import time
import sys
import os
from threading import Thread
from bs4 import BeautifulSoup
from IPy import IP

from Utilities.Useful_functions import getHashes
from Utilities.Useful_functions import find
from Utilities.Print_functions import __print_verbosity
from Core.adbClass import ThreadAnalyzer,Proxy,Adb,getTags

class DynamicAnalysis():
    """
    Class taken from DroidBox for Dynamic Analysis
    I will change some functions which I think I can
    do in another way
    """
    def __init__(self,apk):
        '''
        Constructor of the class

        :param str apk: path to apk to analyze
        :return: None
        :rtype: None
        '''
        self.apk = apk
        self.packages = []
        self.permissions = []
        self.outPermissions = [] #this permissions are for others apps
        self.receivers = []
        self.recvsactions = {}
        self.activities = {}
        

        self.mainActivity = None


    def extractingApk(self):
        """
        Extract information from apk, I will use BeautifulSoup instead of
        XML libraries

        :return: None
        :rtype: None
        """
        try:
            manifest = None
            apkName = self.apk
            apkName = os.path.basename(apkName)
            apkName = apkName.replace(".apk","")

            unzipFolder = "apktool-"+apkName

            folders = os.listdir('.')

            if not (unzipFolder in folders):
                actualDirectory = os.getcwd()
                outputFile = actualDirectory + "/" + "apktool-" + apkName
                sentence = 'apktool d '+self.apk+' -o '+outputFile
                print("[+] Unzipping apk")
                subprocess.call(sentence,shell=True)

            manifest = open(unzipFolder+"/AndroidManifest.xml","rb")
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

