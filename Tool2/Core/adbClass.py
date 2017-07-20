#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: adbClass.py
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


class ThreadAnalyzer(Thread):
    """
    This class Will show how many logs have been get it
    A good implementacion from Heritage of Thread :) 
    """

    def __init__(self):
        """
        Constructor we need to overrite father constructor

        :return: None
        :rtype: None
        """
        Thread.__init__(self)
        self.stop = False # When User press CTRL-C we stop the thread
        self.logs = 0

    def stopThread(self):
        """
        Set stop to True, it will stop the thread

        :return: None
        :rtype: None
        """
        self.stop = True

    def increaseLogs(self):
        """
        We need to increase the logs from thread then we could show how many logs we have
    
        :return: None
        :rtype: None
        """
        self.logs = self.logs + 1

    def run(self):
        """
        Main Method from a Thread, here we will show
        user information about how many logs we have 
        collected

        :return: None
        :rtype: None
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

        :return: None
        :rtype: None
        '''

        self.proxy = "burpsuite"
        if ip:
            self.ip = ip
        else:
            self.ip = "127.0.0.1"
            
        if port:
            self.port = port
        else:
            self.port = "8080"

        self.correct = False 

    def startBurp(self):
        '''
        Start Burpsuite in another gnome-terminal

        :return: None
        :rtype: None
        '''
        thread = Thread(target = self.execProgram)
        thread.run()
        if(not self.correct):
            __print_verbosity(1,"[-] Error with burp thread")
            sys.exit(-1)

    def execProgram(self):
        '''
        Function thread will run for burpsuite

        :return: None
        :rtype: None
        '''
        sentence = "burpsuite &"

        try:
            subprocess.call(sentence,shell=True)
            self.correct = True
        except:
            __print_verbosity(1,"[-] Error with burpsuite, if you don't have it, install it to continue")
            self.correct = False
            sys.exit(-1)

## Tags from android 
tags = { 0x1 :   "TAINT_LOCATION",      0x2: "TAINT_CONTACTS",        0x4: "TAINT_MIC",            0x8: "TAINT_PHONE_NUMBER",
         0x10:   "TAINT_LOCATION_GPS",  0x20: "TAINT_LOCATION_NET",   0x40: "TAINT_LOCATION_LAST", 0x80: "TAINT_CAMERA",
         0x100:  "TAINT_ACCELEROMETER", 0x200: "TAINT_SMS",           0x400: "TAINT_IMEI",         0x800: "TAINT_IMSI",
         0x1000: "TAINT_ICCID",         0x2000: "TAINT_DEVICE_SN",    0x4000: "TAINT_ACCOUNT",     0x8000: "TAINT_BROWSER",
         0x10000: "TAINT_OTHERDB",      0x20000: "TAINT_FILECONTENT", 0x40000: "TAINT_PACKAGE",    0x80000: "TAINT_CALL_LOG",
         0x100000: "TAINT_EMAIL",       0x200000: "TAINT_CALENDAR",   0x400000: "TAINT_SETTINGS" }

def getTags(tagUser):
    tagsFound = []

    for tag in tags.keys():
        # AND operation, if are the same number it will be different from 0
        if tagUser & tag != 0:
            tagsFound.append(tags[tag])

    return tagsFound

class Adb():
    '''
    Class which act as an ADB wrapper
    '''

    def __init__(self,emulator = None,proxy = None):
        """ 
        Constructor of the class 

        :param str emulator: emulator name 
        :param str proxy: proxy conf
        :return: None
        :rtype: None
        """
        self.emulator = emulator
        self.proxy = proxy

    def connectADB_byName(self,ip):
        """ 
        Class to connect with adb device for cuckooDroid

        :param str ip: device name
        :return: integer with result 0 correct -1 something went wrong
        :rtype: int
        """
        __print_verbosity(1,"[+] Trying to connect to: %s" % str(ip))
        try:
            IP(ip)
        except ValueError:
            __print_verbosity(1,"[-] Value: %s is not a valid IP" % ip)
            return -1
        kill_server = """adb kill-server"""
        adb_connect = "adb connect %s" % str(ip)

        subprocess.call(kill_server,shell=True)

        returned_string = subprocess.check_output(adb_connect,shell=True)

        if "unable to connect" in str(returned_string):
            __print_verbosity(1,"[-] It's not possible to connect that IP with adb")
            return -1

        if "already connected to" in str(returned_string):
            counter = 0
            while "already connected to" in str(returned_string):
                subprocess.call(kill_server,shell=True)
                returned_string = subprocess.check_output(adb_connect,shell=True)
                counter += 1
                if counter == 3:
                    break

            if counter == 3: # not possible to connect
                __print_verbosity(1,"[+] It looks that you have a problem connecting with your device")
                respuesta = ''
                while respuesta != 'y' or respuesta != 'n':
                    respuesta = input("Do you want to try even with problems?[y/n]")
                    respuesta = respuesta.lower()

                if respuesta == 'y':
                    return 0
                else:
                    return -1
            else:
                __print_verbosity(0,"[+] Now you are connected to the device: %s" % str(ip))
                return 0
        if 'connected to' in str(returned_string):
            __print_verbosity(0,"[+] Now you are connected to the device: %s"%str(ip))
            return 0

    def startEmulatorProxy(self):
        """
        Start android emulator to install the apk and start analyzer with Burpsuite proxy
        for DroidBox

        :return: None
        :rtype: None
        """
        if self.emulator == None:
            __print_verbosity(1,'[-] Specify emulator name')
            sys.exit(-1)
        if self.proxy == None:
            __print_verbosity(1,'[-] Specify Proxy')
            sys.exit(-1)
        
        system = find("images/system.img")
        ramdisk = find("images/ramdisk.img")
        sentence = 'gnome-terminal --command "emulator -avd '+self.emulator+' -http-proxy '+self.proxy.ip+':'+self.proxy.port+' -system '+system+' -ramdisk '+ramdisk+' -wipe-data -prop dalvik.vm.execution-mode=int:portable"'
        try:
            __print_verbosity(1,"[+] Exec Emulator")
            #print(sentence)
            #input()
            os.system(sentence)
            self.correct = True
        except Exception as e:
            self.correct = False
            __print_verbosity(2,"[-] Error with emulator: %s" % str(e))
            sys.exit(-1)

    def startEmulator(self):
        """
        Start android emulator to install the apk and start analyzer
        for DroidBox

        :return: None
        :rtype: None
        """
        if self.emulator == None:
            print('[-] Specify emulator name')
            sys.exit(-1)
        
        system = find("images/system.img")
        ramdisk = find("images/ramdisk.img")
        sentence = 'gnome-terminal --command "emulator -avd '+self.emulator+' -system '+system+' -ramdisk '+ramdisk+' -wipe-data -prop dalvik.vm.execution-mode=int:portable"'
        try:
            print("[+] Exec Emulator")
            #print(sentence)
            #input()
            os.system(sentence)
            self.correct = True
        except Exception as e:
            self.correct = False
            print("[-] Error with emulator: %s"%str(e))
            sys.exit(-1)

    def cleanAdbLogcat(self):
        """
        Clean logcat to start the analysis

        :return: None
        :rtype: None
        """
        subprocess.call(["adb","logcat","-c"])

    def droidboxLogCat(self):
        '''
        Logcat execute for droidbox with proper arguments

        :return: pipe to adb input/output
        :rtype: subprocess.PIPE
        '''
        adb = subprocess.Popen(["adb", "logcat", "DroidBox:W", "dalvikvm:W", "ActivityManager:I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return adb

