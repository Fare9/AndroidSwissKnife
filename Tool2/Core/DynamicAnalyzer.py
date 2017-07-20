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


import os,sys,subprocess,time,json,pprint

from Utilities.Print_functions import __print_verbosity
from Core.adbClass import Adb,Proxy,ThreadAnalyzer
from Core.ApktoolAnalysis import StaticComleteAnalysis
from Utilities.Useful_vars import OKGREEN,ENDC
from Utilities.Useful_functions import progressBar

class DroidBox():

    def __init__(self,apk,DeviceName,burp):
        '''
        Constructor of the class, it will check the inputs

        :return: None
        :rtype: None
        '''
        if not apk:
            print('[-] You must specify apk with -a')
            sys.exit(-1)
        if not DeviceName:
            print('[-] You must specify device name with --device')
            sys.exit(-1)

        # check if apk is relative or absolute path
        if not os.path.isabs(apk):
            # if relative, well get absolute path
            apk = os.path.abspath(apk)

        self.apk = apk
        self.deviceName = DeviceName
        self.mainActivity = None
        self.packages = None
        self.adb = None

        self.sendsms = {}
        self.phonecalls = {}
        self.cryptousage = {}
        self.dexclass = {}
        self.dataleaks = {}
        self.opennet = {}
        self.sendnet = {}
        self.recvnet = {}
        self.closenet = {}
        self.fdaccess = {}
        self.servicestart = {}
        self.accessedfiles = {}
        self.errors = []  # If some line get an error, why don't we show it?

        self.burp = burp
        # burpsuite proxy
        if self.burp:
            self.prox = Proxy()
        else:
            self.prox = None

    def __connectWithAdb(self):
        '''
        Method to connect with adb to DroidMon emulator

        :return: None
        :rtype: None
        '''
        adbHandler = Adb(self.deviceName,self.prox)
        # connect to ADB
        if self.burp:
            self.__startBurp()
            adbHandler.startEmulatorProxy()
        else:
            adbHandler.startEmulator()

        # static analysis
        self.__staticAnalysis()
        # clean logcat
        adbHandler.cleanAdbLogcat()

        self.__startMonkeyRunner()

        

        self.adb = adbHandler.droidboxLogCat()

    def __runMachine(self):
        '''
        Run everything with while True

        :return: None
        :rtype: None
        '''
        applicationStarted = 0
        stringApplicationStarted = "Start proc %s" % packages
        logcatOutput = None

        while True:
            try:
                logcatOutput = str(self.adb.stdout.readline())
            except Exception as e:
                print("[-] Error getting logcatOutput: " + str(e))
                break
            try:
                # print(logcatOutput)
                if not logcatOutput:
                    raise Exception("[-] We have lost the connection with ADB, try to wait for emulator.")
            except Exception as e:
                print("[-] Error getting logcatOutput [2]: " + str(e))
                break
            try:
                if stringApplicationStarted in logcatOutput:
                    applicationStarted = 1
                    break
            except Exception as e:
                print("[-] Error getting logcatOutput [3]: " + str(e))
                break

        if applicationStarted == 0:
            print("[-] Application didn't started")
            # Now kill adb (It was a background process)
            os.kill(self.adb.pid, signal.SIGKILL)
            sys.exit(-1)

        print("[+] Okey Application started, now start analysis")
        logthread = ThreadAnalyzer()
        logthread.start()

        timestamp = time.time()  # get current time
        while 1:
            try:
                logcatOutput = adb.stdout.readline()
                if not logcatOutput:
                    # If something went wrong raise error
                    raise Exception("[-] We have lost the connection with ADB.")

                # We have logs which start with DroidBox word
                # We are using custom system and custom ramdisk
                # then we have prepare applications to have this Flag
                try:
                    # print(logcatOutput)
                    # input()
                    boxlog = logcatOutput.decode().split('DroidBox:')
                except Exception as e:
                    print("[-] Error Decoding: " + str(e))
                    continue
                if len(boxlog) > 1:
                    try:
                        sentence = json.loads(boxlog[1])
                        # look for Dexclassloader
                        if 'DexClassLoader' in sentence:
                            sentence['DexClassLoader']['type'] = 'dexload'
                            self.dexclass[time.time() - timestamp] = sentence['DexClassLoader']
                            logthread.increaseLogs()

                        # look for service started
                        if 'ServiceStart' in sentence:
                            # service started
                            sentence['ServiceStart']['type'] = 'service'
                            self.servicestart[time.time() - timestamp] = sentence['ServiceStart']
                            logthread.increaseLogs()

                        # received data from net
                        if 'RecvNet' in sentence:
                            host = sentence['RecvNet']['srchost']
                            port = sentence['RecvNet']['srcport']
                            recvdata = {'type': 'net read', 'host': host, 'port': port,
                                        'data': sentence['RecvNet']['data']}
                            self.recvnet[time.time() - timestamp] = recvdata
                            logthread.increaseLogs()


                        # fdaccess
                        if 'FdAccess' in sentence:
                            self.accessedfiles[sentence['FdAccess']['id']] = codecs.decode(sentence['FdAccess']['path'],
                                                                                      'hex')  # convert HEX to string, now we have the path

                        # file read or write   
                        if 'FileRW' in sentence:
                            sentence['FileRW']['path'] = accessedfiles[sentence['FileRW']['id']]
                            if sentence['FileRW']['operation'] == 'write':
                                # if operation is write, then type is file write
                                sentence['FileRW']['type'] = 'file write'
                            else:
                                # in the other hand, if it is read access
                                sentence['FileRW']['type'] = 'file read'

                            self.fdaccess[time.time() - timestamp] = sentence['FileRW']
                            logthread.increaseLogs()

                        # opened network connection log
                        if 'OpenNet' in sentence:
                            self.opennet[time.time() - timestamp] = sentence['OpenNet']
                            logthread.increaseLogs()

                        # closed socket
                        if 'CloseNet' in sentence:
                            self.closenet[time.time() - timestamp] = sentence['CloseNet']
                            logthread.increaseLogs()

                        # outgoing network activity log
                        if 'SendNet' in sentence:
                            sentence['SendNet']['type'] = 'net write'
                            self.sendnet[time.time() - timestamp] = sentence['SendNet']

                            logthread.increaseLogs()

                        if 'DataLeak' in sentence:
                            my_time = time.time() - timestamp
                            sentence['DataLeak']['type'] = 'leak'
                            sentence['DataLeak']['tag'] = adbClass.getTags(int(sentence['DataLeak']['tag'], 16))
                            self.dataleaks[my_time] = sentence['DataLeak']
                            logthread.increaseLogs()

                            if sentence['DataLeak']['sink'] == 'Network':
                                sentence['DataLeak']['type'] = 'net write'
                                self.sendnet[my_time] = sentence['DataLeak']
                                logthread.increaseLogs()

                            elif sentence['DataLeak']['sink'] == 'File':
                                # If it is a file
                                sentence['DataLeak']['path'] = accessedfiles[sentence['DataLeak']['id']]

                                # get if it's write or read
                                if sentence['DataLeak']['operation'] == 'write':
                                    sentence['DataLeak']['type'] = 'file write'
                                else:
                                    sentence['DataLeak']['type'] = 'file read'
                                # add to fdaccess
                                self.fdaccess[my_time] = sentence['DataLeak']
                                logthread.increaseLogs()

                            elif sentence['DataLeak']['sink'] == 'SMS':
                                sentence['DataLeak']['type'] = 'sms'
                                self.sendsms[my_time] = sentence['DataLeak']
                                logthread.increaseLogs()

                        # sent sms log
                        if 'SendSMS' in sentence:
                            sentence['SendSMS']['type'] = 'sms'
                            self.sendsms[time.time() - timestamp] = sentence['SendSMS']
                            logthread.increaseLogs()

                        # phone call log
                        if 'PhoneCall' in sentence:
                            sentence['PhoneCall']['type'] = 'call'
                            self.phonecalls[time.time() - timestamp] = sentence['PhoneCall']
                            logthread.increaseLogs()

                        # crypto api usage log
                        if 'CryptoUsage' in sentence:
                            sentence['CryptoUsage']['type'] = 'crypto'
                            self.cryptousage[time.time() - timestamp] = sentence['CryptoUsage']
                            logthread.increaseLogs()

                    except ValueError as e:
                        print("[-] ValueError: " + str(e))
                        self.errors.append(boxlog[1])
                        pass
            except KeyboardInterrupt as e:
                try:
                    # If CTRL-C pressed stop thread
                    logthread.stopThread()
                    logthread.join()
                finally:
                    break;
            except Exception as e:
                print("[-] Error parsing adb logcat output: " + str(e))

        # KILL ADB LOGCAAAT
        os.kill(adb.pid, signal.SIGKILL)
        # Done? Store the objects in a dictionary, transform it in a JSON object and return it
        output = dict()
        # Sort the items by their key
        output["dexclass"] = self.dexclass
        output["servicestart"] = self.servicestart

        output["recvnet"] = self.recvnet
        output["opennet"] = self.opennet
        output["sendnet"] = self.sendnet
        output["closenet"] = self.closenet

        output["accessedfiles"] = self.accessedfiles
        output["dataleaks"] = self.dataleaks

        output["fdaccess"] = self.fdaccess
        output["sendsms"] = self.sendsms
        output["phonecalls"] = self.phonecalls
        output["cryptousage"] = self.cryptousage

        # sometimes there are errors in system image, but no problem 
        # we can show the logs with errors (usually crypto)
        output["errors"] = self.errors  

        pp = pprint.PrettyPrinter(indent=4)

        pp.pprint(output)

    def __staticAnalysis(self):
        '''
        Method to get static info, necessary for monkeyFaren
        
        :return: None
        :rtype: None
        '''
        staticAnalysis = StaticComleteAnalysis(self.apk,None)
        staticAnalysis.extractingApkInfo()
        staticAnalysis.showInfo()

        self.mainActivity = staticAnalysis.mainActivity
        self.packages = staticAnalysis.packages

        # If some error parsing AndroidManifest something strange happened, then exit
        if not self.mainActivity or not self.packages:
            print('[-] There\'s no main activity or packages,you can\'t continue')
            sys.exit(0)

    def __startMonkeyRunner(self):
        '''
        Method to start monkeyFaren in another process with subprocess.call

        :return: None
        :rtype: None
        '''
        ret = subprocess.call(['monkeyrunner', 'Libs/monkeyFaren.py', self.apk, self.packages, self.mainActivity],
                              stderr=subprocess.PIPE, cwd=os.path.dirname(os.path.realpath(__file__)))

        if ret == 1:
                print("[-] Failed to start monkeyrunner")
                sys.exit(1)

    def __startBurp(self):
        '''
        Start burpsuite if user has decided it

        :return: None
        :rtype: None
        '''
        prox.startBurp()
        print(OKGREEN)
        progressBar()
        print(ENDC)


    def run(self):
        '''
        Exec everything together for DroidBox

        :return: None
        :rtype: None
        '''
        self.__connectWithAdb()
        self.__runMachine()