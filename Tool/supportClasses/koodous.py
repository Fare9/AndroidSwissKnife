'''
    Koodous is a free Antivirus for Android
    with contributions from the community.

    It will works as a quick analyzer
'''

import hashlib
import requests
import sys
import os
import json
import time
import pprint

####### RES API TOKEN FROM KOODOUS USER
token = 'a45bbf2f998215f08475cde600dae6eb3fd91630'


class KoodousAnalyzer():
    '''
        Class to connect with koodous rest API
    '''

    def __init__(self, apk, upload):
        self.apk = apk
        self.jsonOutput = ''
        self.hash = self.getSHA256()
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
                    401: "APK doesn't exist",
                    405: "waiting finish analysis"
        }

    def getSHA256(self):
        '''
            get SHA256 hash from the APK
            it will be for the Koodous Rest API
        :return:
        '''
        try:
            sha256 = hashlib.sha256()
            f = open(self.apk, 'rb')

            # now we read the apk and create hashes
            while True:
                data = f.read(512)
                if not data:
                    break

                sha256.update(data)

            return sha256.hexdigest()
        except Exception as e:
            print ("[-] ERROR getting SHA256 from file: "+str(e))
            sys.exit(-1)

    def analyzeApk(self):
        '''
            Get if exists some analysis from an apk
        :return:
        '''
        if token == '':
            return
        print ("[+] Hash to analyze with koodous: "+self.hash)
        try:
            url_koodous = "https://api.koodous.com/apks/%s/analysis" % self.hash
            r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})
            if r.status_code == 200:
                print("[+] Everything was okay")
                self.jsonOutput = r.json()
            elif r.status_code == 404:
                print("[+] That APK doesn't exist")
                if self.upload:
                    self.jsonOutput = self.upload_and_analyze()
                    print("Report to URL: ")
                    print(url_koodous)
                else:
                    self.jsonOutput = ''
            else:
                print("[-] There was a problem: "+str(r.text))
                print("[-] Koodous error: "+str(self.status_code[r.status_code]))
                self.jsonOutput = ''
        except Exception as e:
            print("[-] Error while getting koodous response: "+str(e))
            print("[-] Koodous error: "+str(self.status_code[r.status_code]))

    def upload_and_analyze(self):
        '''
            Method to get an upload file URL and upload the file,
            then wait for the analysis, finally get report
        '''
        if token == '':
            return

        print ("[+] Getting upload url from koodous")
        try:
            url_koodous = "https://api.koodous.com/apks/%s/get_upload_url" % self.hash
            r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

            if r.status_code == 200:
                print("[+] Everything was okay getting url")

                
                j = r.json()

                print("[+] Uploading apk to: "+str(j['upload_url']))


                files = {'file': open(self.apk,'rb')}

                s = requests.post(url=j['upload_url'],files=files)

                if s.status_code == 201: # 201 when created the file 
                    print('[+] Everything Okay uploading file')

                    # now let start analysis
                    print('[+] Let\'s start analysis')
                    url_koodous = "https://api.koodous.com/apks/%s/analyze" % self.hash
                    r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

                    if r.status_code == 200:
                        print('[+] Analysis started')

                        # check if has finished

                        url_koodous = "https://api.koodous.com/apks/%s/analysis" % self.hash
                        r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

                        i = 0
                        constant_string = 'Waiting for the report'
                        while r.status_code == 405:
                            # show dots in string
                            show_string = constant_string[0:i]
                            sys.stdout.write(show_string)
                            sys.stdout.flush()
                            i += 1
                            if i == (len(constant_string) + 1):
                                i = 0

                            time.sleep(0.2)
                            sys.stdout.write("\033[K\r")
                            sys.stdout.flush()
                            r = requests.get(url=url_koodous, headers={'Authorization': 'Token %s' % token})

                        return r.json()
                    else:
                        print("[-] Koodous error: "+str(self.status_code[r.status_code]))

                else:
                    print("[-] Koodous error: "+str(self.status_code[s.status_code]))
                    print('[-] Something went wrong uploading file, check your internet connectivity or API key')
            
            else:
                print("[-] Koodous error: "+str(self.status_code[r.status_code]))
        except Exception as e:
            print("[-] There was an error in upload_and_analyze: "+str(e))
            return None

if __name__ == "__main__":
    koodous = KoodousAnalyzer('/tmp/ojete.apk',True)
    koodous.analyzeApk()
    pprint.pprint(koodous.jsonOutput,indent=4)
