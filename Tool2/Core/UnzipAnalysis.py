#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: UnzipAnalysis.py
'''

'''
    Functions for analysis with unzip
'''
import os,sys,subprocess
try:
    import zipfile
except Exception:
    print("[-] You need zipfile (try with --install)")
    sys.exit(-1)
from Utilities.Print_functions import __print_verbosity
from Utilities.Print_functions import __print_list
from Utilities.Useful_vars import apkInformation

def unzipFunc(file, outputName, regularExpresion):
    '''
    Unzip apk to unzip folder, then use this folder for other functions

    :param str file: input apk to unzip and analyze
    :return: None
    :rtype: None
    '''

    __print_verbosity(1,"[+] Creating Directory from apk to unzip output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    # create name directory as: actualDirectory/unzip-outputName
    outputFile = actualDirectory + "/" + "unzip-" + outputName

    try:
        # unzip the file
        zip_ref = zipfile.ZipFile(file,'r')
        zip_ref.extractall(outputFile)
        zip_ref.close()
        input("[!] Press enter")
        __readCertificate(outputFile)
        input("[!] Press enter")
        __listAsset(outputFile)
        input("[!] Press enter")
        __listCode(outputFile)
        input("[!] Press enter")
        __showStrings(outputFile, regularExpresion)
    except Exception as e:
        os.chdir(actualDirectory)
        __print_verbosity(2,"[Debug] Error: %s" % (str(e)))


def __readCertificate(directory):
    '''
    Module to read the certificate from directory that unzip has created

    :param str directory: output directory from unzipFunc
    :return: None
    :rtype: None
    '''

    actualDirectory = os.getcwd()

    __print_verbosity(1,'[+] Change directory to: %s' % (directory))
    os.chdir(directory)

    __print_verbosity(0,'[+] Reading the application certificate...')
    statement = 'keytool -printcert -file ./META-INF/CERT.RSA'
    try:
        certficate = subprocess.check_output(statement,shell=True)
        __print_verbosity(0,certficate.decode('utf-8'))
        apkInformation['Certificate'] = certficate.decode('utf-8')



    except Exception as e:
        __print_verbosity(2,"[Debug] Error: %s" % (str(e)))
        __print_verbosity(1,"[-] Maybe you need keytool...")

    __print_verbosity(1,'[+] Returning to Directory: %s' % (actualDirectory))
    os.chdir(actualDirectory)


def __listAsset(directory):
    '''
    Module to list assets directory (if exists) maybe you can find interesting files

    :param str directory: output directory from unzipFunc
    :return: None
    :rtype: None
    '''
    actualDirectory = os.getcwd()
    apkInformation['assets'] = []

    __print_verbosity(1,'[+] Change directory to: %s' % (directory))
    os.chdir(directory)

    __print_verbosity(0,'[+] Looking for assets directory...')
    subdirs = os.listdir('.')

    if "assets" in subdirs:
        __print_verbosity(1,'[+] Okey I think that we have assets file...')
        # show in a cool way
        for root, dirs, files in os.walk('./assets'):
            for file in files:
                __print_verbosity(0,"[+] File assets: %s" % (os.path.join(root, file)))
                apkInformation['assets'].append(os.path.join(root, file))
    else:
        __print_verbosity(0,'[+] There\'s no assets file')

    __print_verbosity(1,"[+] Returning to Directory: %s" % (actualDirectory))
    os.chdir(actualDirectory)


def __listCode(directory):
    '''
    Module to list all possible code files now we will list .apk, .jar, .class from unzip content

    :param str directory: output directory from unzipFunc
    :return: None
    :rtype: None
    '''
    apkInformation['CodeFiles'] = {}
    apkInformation['CodeFiles']['APK'] = []
    apkInformation['CodeFiles']['JAR'] = []
    apkInformation['CodeFiles']['CLASS'] = []
    __print_verbosity(1,'[+] Showing possible code files inside unzip project')
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.apk'):
                pathFile = os.path.join(root, file)
                __print_verbosity(0,pathFile)
                apkInformation['CodeFiles']['APK'].append(pathFile.decode('utf-8'))
            elif file.endswith('.jar'): 
                pathFile = os.path.join(root, file)
                __print_verbosity(0,pathFile)
                apkInformation['CodeFiles']['JAR'].append(pathFile.decode('utf-8'))
            elif file.endswith('.class'):
                pathFile = os.path.join(root, file)
                __print_verbosity(0,pathFile)
                apkInformation['CodeFiles']['CLASS'].append(pathFile.decode('utf-8'))


def __showStrings(directory, regEx):
    '''
    Module to show strings from .dex file or files in general with some regular Expressions

    :param str directory: output directory from unzipFunc
    :param str regEx: regular expression to search in code files
    :return: None
    :rtype: None
    '''

    javaclassRegEx = '"L[^;]+?;"'  # Objects or classes (start by L in smali code)
    urlRegEx = '"https?:"'  # http or https
    urlBase64RegEx = '"aHR0cDo|aHR0cHM6L"'  # http or https in base64
    emails = '"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]"' # look for emails in code
    actualDirectory = os.getcwd()

    apkInformation['strings'] = {}
    apkInformation['strings']['javaclasses'] = []
    apkInformation['strings']['urls'] = []
    apkInformation['strings']['urlsB64'] = []
    apkInformation['strings']['email'] = []
    apkInformation['strings']['other'] = []
    __print_verbosity(1,'[+] Change diretory to: %s' % (directory))
    os.chdir(directory)

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.dex'): # for compiled files
                __print_verbosity(0,'[+] Showing strings for: %s' % (os.path.join(root, file)))
                try:
                    javaClass = subprocess.check_output("strings %s | egrep %s" % (os.path.join(root, file),javaclassRegEx),shell=True)
                    __print_list(0,javaClass.decode('utf-8'),'\n')
                    apkInformation['strings']['javaclasses'].append({os.path.join(root, file):javaClass.decode('utf-8')})
                except CalledProcessError:
                    pass
                try:
                    url = subprocess.check_output("strings %s | egrep %s"  % (os.path.join(root, file),urlRegEx))
                    __print_list(0,url.decode('utf-8'),'\n')
                    apkInformation['strings']['urls'].append({os.path.join(root, file):url.decode('utf-8')})
                except CalledProcessError:
                    pass
                try:
                    urlb64 = subprocess.check_output("strings %s | egrep %s" % (os.path.join(root, file),urlBase64RegEx))
                    __print_list(0,urlb64.decode('utf-8'),'\n')
                    apkInformation['strings']['urlsB64'].append({os.path.join(root, file):urlb64.decode('utf-8')})
                except CalledProcessError:
                    pass
                try:
                    emails = subprocess.check_output("strings %s | egrep %s" % (os.path.join(root, file),emails))
                    __print_list(0,emails.decode('utf-8'),'\n')
                    apkInformation['strings']['email'].append({os.path.join(root, file):emails.decode('utf-8')})
                except CalledProcessError:
                    pass
                if regEx != '':
                    try:
                        other = subprocess.check_output("strings %s | egrep %s" % (os.path.join(root, file),regEx))
                        __print_list(0,other.decode('utf-8'),'\n')
                        apkInformation['strings']['other'].append({os.path.join(root, file):other.decode('utf-8')})
                    except CalledProcessError:
                        pass
            else: # another files
                __print_verbosity(0,'[+] Showing strings for: %s' % (os.path.join(root, file)))
                try:
                    javaClass = subprocess.check_output("cat %s | egrep %s" % (os.path.join(root, file),javaclassRegEx),shell=True)
                    __print_list(0,javaclasses.decode('utf-8'),'\n')
                    apkInformation['strings']['javaclasses'].append({os.path.join(root, file):javaClass.decode('utf-8')})
                except CalledProcessError:
                    pass
                try:
                    url = subprocess.check_output("cat %s | egrep %s"  % (os.path.join(root, file),urlRegEx))
                    __print_list(0,url.decode('utf-8'),'\n')
                    apkInformation['strings']['urls'].append({os.path.join(root, file):url.decode('utf-8')})
                except CalledProcessError:
                    pass
                try:
                    urlb64 = subprocess.check_output("cat %s | egrep %s" % (os.path.join(root, file),urlBase64RegEx))
                    __print_list(0,urlb64.decode('utf-8'),'\n')
                    apkInformation['strings']['urlsB64'].append({os.path.join(root, file):urlb64.decode('utf-8')})
                except CalledProcessError:
                    pass
                try:
                    emails = subprocess.check_output("cat %s | egrep %s" % (os.path.join(root, file),emails))
                    __print_list(0,emails.decode('utf-8'),'\n')
                    apkInformation['strings']['email'].append({os.path.join(root, file):emails.decode('utf-8')})
                except CalledProcessError:
                    pass
                if regEx != '':
                    try:
                        other = subprocess.check_output("cat %s | egrep %s" % (os.path.join(root, file),regEx))
                        __print_list(0,other.decode('utf-8'),'\n')
                        apkInformation['strings']['other'].append({os.path.join(root, file):other.decode('utf-8')})
                    except CalledProcessError:
                        pass
    __print_verbosity(0,"[+] Returning to Directory: %s" % (actualDirectory))
    os.chdir(actualDirectory)