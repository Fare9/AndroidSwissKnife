#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: Koodous.py
'''


'''
    API Client for koodous
'''
import requests
import sys
import os
import json
import time
import pprint

from Utilities.Useful_functions import getHashes
from Utilities.Print_functions import __print_verbosity

####### RES API TOKEN FROM KOODOUS USER
token = ''


class KoodousAnalyzer():

    def __init__(self, apk, upload):
        if not apk:
            print("[-] Use --help or -h to check help")
            sys.exit(0)
        self.apk = apk
        self.jsonOutput = ''
        self.md5,self.sha1,self.sha256 = getHashes(self.apk)
        self.upload = upload
        self.status_code = {
                    200: "All is done",
                    201: "Created",
                    415: "It,s not a apk",
                    412: "Policy exception",
                    408: "The url is lapsed",
                    409: "Apk already exist in our database",
                    401: "Invalid token",
                    429: "Api limit reached",
                    404: "Doesn't exist",
                    405: "waiting finish analysis"
        }

    def analyzeApk(self):
        '''
            Get if exists some analysis from an apk

        :return:
        '''
        if token == '':
            __print_verbosity(0,'[-] You need to write your token from koodous')
            return

        __print_verbosity(0,"[+] Hash to analyze with koodous: %s" % self.sha256)
        try:
            url_koodous = "https://api.koodous.com/apks/%s/analysis" % self.sha256
            r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})
            if r.status_code == 200:
                __print_verbosity(1,"[+] Everything was okay")
                self.jsonOutput = r.json()
            elif r.status_code == 404:
                __print_verbosity(1,"[+] That APK doesn't exist")
                if self.upload:
                    self.jsonOutput = self.upload_and_analyze()
                    __print_verbosity(1,"Report to URL: ")
                    __print_verbosity(0,url_koodous)
                else:
                    self.jsonOutput = ''
            else:
                __print_verbosity(2,"[-] There was a problem: %s" % str(r.text))
                __print_verbosity(1,"[-] Koodous error: %s" % str(self.status_code[r.status_code]))
                self.jsonOutput = ''
        except Exception as e:
            __print_verbosity(2,"[-] Error while getting koodous response: %s" % str(e))
            __print_verbosity(1,"[-] Koodous error: %s" % str(self.status_code[r.status_code]))

    def upload_and_analyze(self):
        '''
            Method to get an upload file URL and upload the file,
            then wait for the analysis, finally get report
        '''
        if token == '':
            __print_verbosity(0,'[-] You need to write your token from koodous')
            return

        __print_verbosity(1,"[+] Getting upload url from koodous")
        try:
            url_koodous = "https://api.koodous.com/apks/%s/get_upload_url" % self.hash
            r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

            if r.status_code == 200:
                __print_verbosity(1,"[+] Everything was okay getting url")
                
                j = r.json()


                __print_verbosity(0,"[+] Uploading apk to: %s" % str(j['upload_url']))


                files = {'file': open(self.apk,'rb')}

                s = requests.post(url=j['upload_url'],files=files)

                if s.status_code == 201: # 201 when created the file 
                    __print_verbosity(1,'[+] Everything Okay uploading file')

                    # now let start analysis
                    __print_verbosity(0,'[+] Let\'s start analysis')
                    url_koodous = "https://api.koodous.com/apks/%s/analyze" % self.hash
                    r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

                    if r.status_code == 200:
                        __print_verbosity(1,'[+] Analysis started')

                        # check if has finished

                        url_koodous = "https://api.koodous.com/apks/%s/analysis" % self.hash
                        r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

                        i = 0
                        constant_string = 'Waiting for the report...'

                        counter = 0
                        while r.status_code == 405:
                            # show dots in string
                            show_string = constant_string[0:i]
                            sys.stdout.write(show_string)
                            sys.stdout.flush()
                            i += 1
                            if i == (len(constant_string) + 1):
                                i = 0

                            time.sleep(0.2)
                            counter += 1
                            sys.stdout.write("\033[K\r")
                            sys.stdout.flush()

                            if counter == 1500: # I know maybe is too much, but you can't overwhelm the api
                                r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})
                                counter = 0

                        return r.json()
                    else:
                        __print_verbosity(0,"[-] Koodous error: %s" % str(self.status_code[r.status_code]))

                else:
                    __print_verbosity(1,"[-] Koodous error: %s" % str(self.status_code[s.status_code]))
                    __print_verbosity(1,'[-] Something went wrong uploading file, check your internet connectivity or API key')
            
            else:
                __print_verbosity(1,"[-] Koodous error: %s" % str(self.status_code[r.status_code]))
        except Exception as e:
            __print_verbosity(2,"[-] There was an error in upload_and_analyze: %s" % str(e))
            return None