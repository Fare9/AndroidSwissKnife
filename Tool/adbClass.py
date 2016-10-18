#!/usr/bin/env python3

'''
    Classes that will help with android dynamic analysis
    we will use adb to start an emulator, install apk, run
    and also use proxy

    Why another class file with classes? If you create a 
    complex structure nobody can understand it.

    "Nunca lo olvides, luchamos juntos"
'''

import subprocess
import time
import sys
import os
from threading import Thread

from bs4 import BeautifulSoup


class Proxy():

    def __init__(self,ip = None,port = None):
        '''
            Constructor for proxy, we will add some
            basic data
        '''

        self.proxy = "burpsuite"
        if ip == None:
            self.ip = "127.0.0.1"
        else:
            self.ip = ip

        if port == None:
            self.port = "8080"
        else:
            self.port = port

        self.correct = False

    def startBurp(self):
        thread = Thread(target = self.execProgram)
        thread.run()
        if(not self.correct):
            print("[-] Error with burp thread")
            sys.exit(-1)

    def execProgram(self):

        sentence = "burpsuite &"

        try:
            subprocess.call(sentence,shell=True)
            self.correct = True
        except:
            print("[-] Error with burpsuite, if you don't have it, install it to continue")
            self.correct = False
            sys.exit(-1)

class Adb():

    def __init__(self,emulator = None,proxy = None):
        if emulator == None:
            print('[-] Specify emulator name')
            sys.exit(-1)
        else:
            self.emulator = emulator
        self.proxy = proxy


    def startEmulator(self):
        sentence = "emulator -avd "+self.emulator+" -http-proxy "+self.proxy.ip+":"+self.proxy.port
        try:
            subprocess.call(sentence,shell=True)
        except Exception as e:
            print("[-] Error with emulator: "+str(e))
            sys.exit(-1)


class DynamicAnalyzer():
    """
        Class taken from DroidBox for Dynamic Analysis
        I will change some functions which I think I can
        do in another way
    """

    def __init__(self,apk):
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
        """
        try:
            manifest = None
            apkName = self.apk
            apkName = apkName.replace(".apk","")

            unzipFolder = "unzip-"+apkName

            folders = os.listdir('.')

            if not (unzipFolder in folders):
                outputFile = actualDirectory + "/" + "unzip-" + outputName
                sentence = 'unzip '+file+' -d '+outputFile

            manifest = open(unzipFolder+"/AndroidManifest.xml","rb")
            bsObj = BeautifulSoup(manifest.read(),"lxml")

            ## Now start parsing

            # package
            packages= bsObj.findAll("manifest")
            for package in packages:
                self.packages.append(str(package['package']))

            print("[+] Packages: "+str(self.packages))
            # uses-permission
            usespermissions = bsObj.findAll("uses-permission")
            for usespermission in usespermissions:
                self.permissions.append(str(usespermission['android:name']))

            print('[+] Uses-Permissions: '+str(self.permissions))
            # out permissions
            permissions = bsObj.findAll("permission")
            for permission in permissions:
                self.outPermissions.append(str(permission['android:name']))
            print('[+] Permissions: '+str(self.outPermissions))
            #  Receivers and actions from that receiver
            ##  1 Receiver can have 0 or more actions, then actions should be a list
            receivers = bsObj.findAll("receiver")
            for receiver in receivers:
                self.receivers.append(receiver['android:name'])
                actions = receiver.findAll("action")
                self.recvsactions[receiver['android:name']] = list()
                for action in actions:
                    self.recvsactions[receiver['android:name']].append(action['android:name'])

            print("[+] Receivers: "+str(self.receivers))
            print("[+] RecvsActions: "+str(self.recvsactions))
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
            print("[+] Activities: "+str(self.activities))
            # well extract which is the main activity
            for activity in self.activities:
                if "android.intent.action.MAIN" in self.activities[activity]["actions"]:
                    self.mainActivity = activity 
                    break
            print("[+] MainActivity: "+str(self.mainActivity))

        except Exception as e:
            print("[+] Error parsing AndroidManifest: "+str(e))


def progressBar():
    """
        Progress bar for 4 seconds
    """
    print("[+] Loading Burpsuite")
    for i in range(0,26):
        x = i*100/25
        if i != 25:
            sys.stdout.write("["+"="*i+">]"+str(x)+"%\r")
        else:
            sys.stdout.write("["+"="*i+">]"+str(x)+"%\n")
        sys.stdout.flush() 
        time.sleep(0.2)

if __name__ == '__main__':
    '''
    burp = Proxy()
    print("Burp ip: "+burp.ip)
    print("Burp port: "+burp.port)
    burp.startBurp()

    

    adb = Adb(emulator="Sandbox",proxy=burp)
    adb.startEmulator()
    '''
    da = DynamicAnalyzer(apk="prueba.apk")
    da.extractingApk()
