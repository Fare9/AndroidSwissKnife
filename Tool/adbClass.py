#!/usr/bin/env python3

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
import hashlib

from threading import Thread
from bs4 import BeautifulSoup

class threadAnalyzer(Thread):
    """
        This class Will show how many logs have been get it
        A good implementacion from Heritage of Thread :) 
    """

    def __init__(self):
        """
            Constructor we need to overrite father constructor
        """
        Thread.__init__(self)
        self.stop = False # When User press CTRL-C we stop the thread
        self.logs = 0

    def stopThread(self):
        """
            Set stop to True
        """
        self.stop = True

    def increaseLogs(self):
        """
            We need to increase the logs from thread
            the we could show how many logs we have
        """
        self.logs = self.logs + 1

    def run(self):
        """
            Main Method from a Thread, here we will show
            user information about how many logs we have 
            collected
        """
        signs = ['|', '/', '-', '\\']
        counter = 0
        while 1:
            sign = signs[counter % len(signs)]
            sys.stdout.write("[AndroidSwissKnife]     \033[132m[%s] Collected %s sandbox logs\033[1m   (Ctrl-C to view logs)\r" % (sign, str(self.logs)))
            sys.stdout.flush()
            time.sleep(0.5)
            counter = counter + 1
            if self.stop:
                sys.stdout.write("[AndroidSwissKnife]   \033[132m[%s] Collected %s sandbox logs\033[1m%s\r" % ('*', str(self.logs), ' '*25))
                sys.stdout.flush()
                break

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

## Tags from android 
tags = { 0x1 :   "TAINT_LOCATION",      0x2: "TAINT_CONTACTS",        0x4: "TAINT_MIC",            0x8: "TAINT_PHONE_NUMBER",
         0x10:   "TAINT_LOCATION_GPS",  0x20: "TAINT_LOCATION_NET",   0x40: "TAINT_LOCATION_LAST", 0x80: "TAINT_CAMERA",
         0x100:  "TAINT_ACCELEROMETER", 0x200: "TAINT_SMS",           0x400: "TAINT_IMEI",         0x800: "TAINT_IMSI",
         0x1000: "TAINT_ICCID",         0x2000: "TAINT_DEVICE_SN",    0x4000: "TAINT_ACCOUNT",     0x8000: "TAINT_BROWSER",
         0x10000: "TAINT_OTHERDB",      0x20000: "TAINT_FILECONTENT", 0x40000: "TAINT_PACKAGE",    0x80000: "TAINT_CALL_LOG",
         0x100000: "TAINT_EMAIL",       0x200000: "TAINT_CALENDAR",   0x400000: "TAINT_SETTINGS" }

class Adb():

    def __init__(self,emulator = None,proxy = None):
        if emulator == None:
            print('[-] Specify emulator name')
            sys.exit(-1)
        else:
            self.emulator = emulator
        self.proxy = proxy

    def startEmulator(self):
        """
            Start android emulator to install the apk and start analyzer
        """
        system = os.path.abspath("images/system.img")
        ramdisk = os.path.abspath("images/ramdisk.img")
        sentence = 'gnome-terminal --command "emulator -avd '+self.emulator+' -http-proxy '+self.proxy.ip+':'+self.proxy.port+' -system '+system+' -ramdisk '+ramdisk+' -wipe-data -prop dalvik.vm.execution-mode=int:portable"'
        try:
            print("[+] Exec Emulator")
            os.system(sentence)
            self.correct = True
        except Exception as e:
            self.correct = False
            print("[-] Error with emulator: "+str(e))
            sys.exit(-1)

    def cleanAdbLogcat(self):
        """
            Clean logcat to start the analysis
        """
        subprocess.call(["adb","logcat","-c"])

    def execAdbLogcat(self):
        """
            Exec logcat with propert arguments
        """
        adb = subprocess.Popen(["adb", "logcat", "DroidBox:W", "dalvikvm:W", "ActivityManager:I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return adb

        

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

            unzipFolder = "apktool-"+apkName

            folders = os.listdir('.')

            if not (unzipFolder in folders):
                actualDirectory = os.getcwd()
                outputFile = actualDirectory + "/" + "apktool-" + apkName
                sentence = 'apktool d '+self.apk+' -o '+outputFile
                print("[+] Unzipping apk")
                subprocess.call(sentence,shell=True)

            manifest = open(unzipFolder+"/AndroidManifest.xml","rb")
            bsObj = BeautifulSoup(manifest.read())

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
            print("[+] Error parsing AndroidManifest: "+str(e))

    def getHash(self):
        """
            Same way that Droidbox did, I will take
            hashes from apk
        """
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        f = open(self.apk,'rb')

        #now we read the apk and create hashes
        while True:
            data = f.read(512)
            if not data:
                break

            md5.update(data)
            sha1.update(data)
            sha256.update(data)

        return [md5.hexdigest(),sha1.hexdigest(),sha256.hexdigest()]

def getTags(tagUser):
    tagsFound = []

    for tag in tags.keys():
        # AND operation, if are the same number it will be different from 0
        if tagUser & tag != 0:
            tagsFound.append(tags[tag])

    return tagsFound
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
    
    burp = Proxy()
    
    print("Burp ip: "+burp.ip)
    print("Burp port: "+burp.port)
    burp.startBurp()
    input()
    adb = Adb(emulator="Sandbox",proxy=burp)
    adb.startEmulator()
    input()
    time.sleep(2)
    da = DynamicAnalyzer(apk="prueba.apk")
    da.extractingApk()
