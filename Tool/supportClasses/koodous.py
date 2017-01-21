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
import pprint

####### RES API TOKEN FROM KOODOUS USER
token = ''


class KoodousAnalyzer():
    '''
        Class to connect with koodous rest API
    '''

    def __init__(self, apk):
        self.apk = apk
        self.jsonOutput = ''
        self.hash = self.getSHA256()

    def getSHA256(self):
        '''
            get SHA256 hash from the APK
            it will be for the Koodous Rest API
        :return:
        '''
        sha256 = hashlib.sha256()
        f = open(self.apk, 'rb')

        # now we read the apk and create hashes
        while True:
            data = f.read(512)
            if not data:
                break

            sha256.update(data)

        return sha256.hexdigest()

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
            self.jsonOutput = r.json()
        except Exception as e:
            print("[-] Error while getting koodous response: "+str(e))


if __name__ == "__main__":
    koodous = KoodousAnalyzer('/root/Documentos/Ciberseg/Analisis_Estatico/13c4823b9de4e0b5f364b70ee1302055b6dc3dd793ed852d0bf0eb1f8d27c0c9.apk')
    koodous.analyzeApk()
    pprint.pprint(koodous.jsonOutput)