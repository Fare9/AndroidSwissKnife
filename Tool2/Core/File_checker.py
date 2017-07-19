#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: File_checker.py
'''


'''
    Functions to check the APK
'''

import sys
try:
    import magic # get mimetype
except ImportError:
    print('[-] Maybe you need magic (try with --install)')
    sys.exit(-1)
from Utilities.Useful_vars import apkInformation
from Utilities.Useful_functions import getHashes

def checkFile(file):
    '''
    module to get information from the apk: filetype and hashes

    :param str file: input apk file to analyze
    '''
    if not file:
        return
    # first put filename in apkInformation
    apkInformation['file_name'] = file
    print("[+] File: %s" % (str(file)))
    # get mymetype and add it to apkInformation
    print("[+] Getting mime type...")
    mimetype = magic.from_file(file, mime=True)
    apkInformation['mime_type'] = str(mimetype)

    print("[+] Mime type: %s" %(str(mimetype)))

    # get hashes
    print("[+] Getting hashes...")
    md5,sha1,sha256 = getHashes(file)
    print("\t[!] MD5: %s" % (str(md5)))
    print("\t[!] SHA1: %s" % (str(sha1)))
    print("\t[!] SHA256: %s" % (str(sha256)))
    apkInformation['md5'] = str(md5)
    apkInformation['sha1'] = str(sha1)
    apkInformation['sha256'] = str(sha256)