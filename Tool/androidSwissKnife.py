#!/usr/bin/env python3

'''
    
    Application to use with APK to create
    files for Static analysis.


'''

#about me and program
programmer = "Fare9"
version = 0.1

#banner
HEADER  = '\033[95m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

bannerP = [
    '''
     ___      .__   __.  _______  .______        ______    __   _______     
    /   \     |  \ |  | |       \ |   _  \      /  __  \  |  | |       \    
   /  ^  \    |   \|  | |  .--.  ||  |_)  |    |  |  |  | |  | |  .--.  |   
  /  /_\  \   |  . `  | |  |  |  ||      /     |  |  |  | |  | |  |  |  |   
 /  _____  \  |  |\   | |  '--'  ||  |\  \----.|  `--'  | |  | |  '--'  |   
/__/     \__\ |__| \__| |_______/ | _| `._____| \______/  |__| |_______/    
                                                                            
     _______.____    __    ____  __       _______.     _______.             
    /       |\   \  /  \  /   / |  |     /       |    /       |             
   |   (----` \   \/    \/   /  |  |    |   (----`   |   (----`             
    \   \      \            /   |  |     \   \        \   \                 
.----)   |      \    /\    /    |  | .----)   |   .----)   |                
|_______/        \__/  \__/     |__| |_______/    |_______/                 
                                                                            
 __  ___ .__   __.  __   _______  _______                                   
|  |/  / |  \ |  | |  | |   ____||   ____|                                  
|  '  /  |   \|  | |  | |  |__   |  |__                                     
|    <   |  . `  | |  | |   __|  |   __|                                    
|  .  \  |  |\   | |  | |  |     |  |____                                   
|__|\__\ |__| \__| |__| |__|     |_______|                                  
                                                                            
    ''',
    '''
 ▄▄▄       ███▄    █ ▓█████▄  ██▀███   ▒█████   ██▓▓█████▄    
▒████▄     ██ ▀█   █ ▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▓██▒▒██▀ ██▌   
▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▓██ ░▄█ ▒▒██░  ██▒▒██▒░██   █▌   
░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██▀▀█▄  ▒██   ██░░██░░▓█▄   ▌   
 ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░██▓ ▒██▒░ ████▓▒░░██░░▒████▓    
 ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▓   ▒▒▓  ▒    
  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░  ▒ ░ ░ ▒  ▒    
  ░   ▒      ░   ░ ░  ░ ░  ░   ░░   ░ ░ ░ ░ ▒   ▒ ░ ░ ░  ░    
      ░  ░         ░    ░       ░         ░ ░   ░     ░       
                      ░                             ░         
  ██████  █     █░ ██▓  ██████   ██████                       
▒██    ▒ ▓█░ █ ░█░▓██▒▒██    ▒ ▒██    ▒                       
░ ▓██▄   ▒█░ █ ░█ ▒██▒░ ▓██▄   ░ ▓██▄                         
  ▒   ██▒░█░ █ ░█ ░██░  ▒   ██▒  ▒   ██▒                      
▒██████▒▒░░██▒██▓ ░██░▒██████▒▒▒██████▒▒                      
▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░▓  ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░                      
░ ░▒  ░ ░  ▒ ░ ░   ▒ ░░ ░▒  ░ ░░ ░▒  ░ ░                      
░  ░  ░    ░   ░   ▒ ░░  ░  ░  ░  ░  ░                        
      ░      ░     ░        ░        ░                        
                                                              
 ██ ▄█▀ ███▄    █  ██▓  █████▒▓█████                          
 ██▄█▒  ██ ▀█   █ ▓██▒▓██   ▒ ▓█   ▀                          
▓███▄░ ▓██  ▀█ ██▒▒██▒▒████ ░ ▒███                            
▓██ █▄ ▓██▒  ▐▌██▒░██░░▓█▒  ░ ▒▓█  ▄                          
▒██▒ █▄▒██░   ▓██░░██░░▒█░    ░▒████▒                         
▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓   ▒ ░    ░░ ▒░ ░                         
░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░ ░       ░ ░  ░                         
░ ░░ ░    ░   ░ ░  ▒ ░ ░ ░       ░                            
░  ░            ░  ░             ░  ░                         
                                               
        ''',
        '''
                                                                    
 @@@@@@   @@@  @@@  @@@@@@@   @@@@@@@    @@@@@@   @@@  @@@@@@@      
@@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@     
@@!  @@@  @@!@!@@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@!  @@@     
!@!  @!@  !@!!@!@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!  !@!  @!@     
@!@!@!@!  @!@ !!@!  @!@  !@!  @!@!!@!   @!@  !@!  !!@  @!@  !@!     
!!!@!!!!  !@!  !!!  !@!  !!!  !!@!@!    !@!  !!!  !!!  !@!  !!!     
!!:  !!!  !!:  !!!  !!:  !!!  !!: :!!   !!:  !!!  !!:  !!:  !!!     
:!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  :!:  !:!     
::   :::   ::   ::   :::: ::  ::   :::  ::::: ::   ::   :::: ::     
 :   : :  ::    :   :: :  :    :   : :   : :  :   :    :: :  :      
                                                                    
                                                                    
 @@@@@@   @@@  @@@  @@@  @@@   @@@@@@    @@@@@@                     
@@@@@@@   @@@  @@@  @@@  @@@  @@@@@@@   @@@@@@@                     
!@@       @@!  @@!  @@!  @@!  !@@       !@@                         
!@!       !@!  !@!  !@!  !@!  !@!       !@!                         
!!@@!!    @!!  !!@  @!@  !!@  !!@@!!    !!@@!!                      
 !!@!!!   !@!  !!!  !@!  !!!   !!@!!!    !!@!!!                     
     !:!  !!:  !!:  !!:  !!:       !:!       !:!                    
    !:!   :!:  :!:  :!:  :!:      !:!       !:!                     
:::: ::    :::: :: :::    ::  :::: ::   :::: ::                     
:: : :      :: :  : :    :    :: : :    :: : :                      
                                                                    
                                                                    
@@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@                         
@@@  @@@  @@@@ @@@  @@@  @@@@@@@@  @@@@@@@@                         
@@!  !@@  @@!@!@@@  @@!  @@!       @@!                              
!@!  @!!  !@!!@!@!  !@!  !@!       !@!                              
@!@@!@!   @!@ !!@!  !!@  @!!!:!    @!!!:!                           
!!@!!!    !@!  !!!  !!!  !!!!!:    !!!!!:                           
!!: :!!   !!:  !!!  !!:  !!:       !!:                              
:!:  !:!  :!:  !:!  :!:  :!:       :!:                              
 ::  :::   ::   ::   ::   ::        :: ::::                         
 :   :::  ::    :   :     :        : :: ::                          
                                                                    
        '''         

]

    

banner = '''
         ### ###                         ### ###
         #######                         #######
         #######      %s#############%s      #######
             ###     %s###############%s    ###
              ###   %s#################%s  ###
               ###%s####################%s###
                 %s########################
                ###########################%s
        %s###########################################
        ###########################################%s
                ###########################
                ######     #####     ######
                #####       ###       #####
                #####       ###       #####
                ######     #####     ######
                 #########################
                  #######################
                   #####################
                 ###  ###############  ###
                ###  #################  ###
               ###   -----------------   ###
          #######    #################    #######
          #######     ###############     #######
          ### ###      #############      ### ###
                        
                        VERSION: %s
                        PROGRAMMER: %s
'''%(WARNING,ENDC,WARNING,ENDC,WARNING,ENDC,WARNING,ENDC,FAIL,ENDC,WARNING,ENDC,str(version),programmer)

import os #to use operating system commands
import sys
import time
import random
import signal
import sqlite3

####################################
# global variables for input

## will give name for output directory or files
outputName = ''

## will get file name and file from here
apkFile = ''

## use apktool in Analysis
apktoolUse = False

## use unzip in Analysis
unzipUse = False

## use exiftool in Analysis
exiftoolUse = False 

## use jadx in Analysis
jadxUse = False

## use dexdump in Analysis
opcodesUse = False

## regular expression for strings function
regularExpresion = ''

## Get jar
getjar = False

## Variables and flags for apk create with apktool
createAPK = False
folderWithCode = ''
apkOutputName = ''

## use for all analysis
allReal = False

#variable for debugging
debug = True

totalHelp = '''
All help is here...

First use: --apktool

We will use apktool to extract data compressed in your apk, please install
the last version of apktool.
When finished the process of descompressing with apktool, we will read the
AndroidManifest.xml and show some strange data (or not).
After that we will read libraries in apk to find some function that
are stored in .so files and start by Java_ . Then that functions could be
called from app code. New feature that use objdump to get assembly code.
If you added --exiftool flag with --apktool we will extract some meta-data
from some files with special extension.
New feature to find databases (sqlite) show tables and schemas from tables.

Second use: --unzip

If you haven't got enough let's going to start with unzip function.
We will use unzip to extract data compressed in apk, because you know
an apk is like zip file.
Then we will show the certificate from the apk (not good quality but
you will have it in terminal)
Then list assets directory, maybe some cool things can be found here.
Now let's going to show some files can have interesting code.
Finally show some strings in files (for now URLs), you can add some
Regular Expression

Third use: --jadx

If you want to try to get java code, we will use jadx to get it. 
It's not better than smali, but If it works you will have source code

Fourth use: --opcodes

Get all instructions, operands used in classes and methods in the bytecode in opcode-name.txt
Get headers of classes and methods in summary-name.txt
Get aditional information about headers like classes' id and superclasses... in sumaryDetails-name.txt
Get the receivers from code that are in AndroidManifest and not. (ORIGINAL IDEA: https://github.com/AndroidWordMalware/malware-samples/blob/master/tools/receiversFinder.py)

Fifth use: --get-jar

Get jar from apk with dex2jar, then get a folder with the jar file
unzipped, you can create java file to call or test classes from this 
jar file.


Final Use: --all

Everything put together, live of color and music.
'''
######################################

def printDebug(string):

    global debug
    if debug:
        print (string)

def install():

    if os.geteuid() != 0:
        print("[-] You need to be root to install packages")
        exit(-1)

    os.mkdir("Tools")

    actualDirectory = os.getcwd()


    print("[+] Creating symbolic links for androidSwissKnife")

    os.system("chmod +x $PWD/androidSwissKnife.py")
    os.system("ln -sf $PWD/androidSwissKnife.py /usr/bin/androidSwissKnife")
    os.system("chmod +x $PWD/manifestDecoder.py")
    os.system("ln -sf $PWD/manifestDecoder.py /usr/bin/manifestDecoder.py")

    print("[+] Now you can call the tool anywhere with: androidSwissKnife")
    print("[+] Going to Directory Tools")
    os.chdir("Tools")
    

    print("[+] Installing last version of apktool")
    os.system("wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.2.0.jar")

    os.system("chmod +x ./apktool_2.2.0.jar")

    os.system("ln -sf $PWD/apktool_2.2.0.jar /usr/bin/apktool")


    print("[+] Installing last version of jadx")

    os.system("git clone https://github.com/skylot/jadx.git")
    os.chdir("jadx")
    
    os.system("./gradlew dist")
    os.system("ln -s $PWD/build/jadx/bin/jadx /usr/bin/jadx-script")
    os.system("ln -s $PWD/build/jadx/bin/jadx-gui /usr/bin/jadx-gui")
    
    os.chdir("..")#Go to Tools
    print("[+] Installing exiftool")
    os.system("sudo apt-get install exiftool")

    print("[+] Installing unzip (if you don't have it yet)")
    os.system("sudo apt-get install unzip")

    print('[+] Installing pip3 ')
    os.system("sudo apt-get install python3-pip")

    print('[+] Installing libraries')
    os.system("pip3 install bytecode")
    
    os.system("sudo apt-get install lib32z1 lib32stdc++6")

    print("[!] Please Install at your own Android SDK and NDK from Android webpage")
    print("\t[+] Then add bin and tools folders from  sdk and ndk to /usr/bin path")
    print("[+] Returning to: "+actualDirectory)

##################################### FOR APKTOOL ###################################
def createApktoolFunc(file):
    '''
        Module to get directory with apk resolution
        from apktool, well we need apktool
    '''  
    global outputName
    global exiftoolUse

    print ("[+] Creating Directory from apk to apktool output...")
    actualDirectory = os.getcwd() #get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    #create name directory as: actualDirectory/apktool-outputName
    outputFile = actualDirectory + "/" + "apktool-" + outputName
    sentence = 'apktool d '+file+' -o '+outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
        readAndroidManifest(outputFile)
        input("[!] Press enter")
        readLibraries(outputFile)
        input("[!] Press enter")

        if exiftoolUse:
            extractMetaData(outputFile)
            input("[!] Press enter")

        readDatabases(outputFile)
        input("[!] Press enter")
    except Exception as e:
        os.chdir(actualDirectory)
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need apktool...")


def readAndroidManifest(directory):

    '''
        Module to read AndroidManifest we will add some 
        features from static analysis

        Please add what you want if you thing something is strange
    '''

    global WARNING
    global FAIL
    global ENDC
    actualDirectory = os.getcwd() #to return after analysis of AndroidManifest

    #change to apktool directory and read AndroidManifest.xml
    print('[+] Change directory to: '+directory)
    os.chdir(directory)

    amFile = open('AndroidManifest.xml','rb')
    xmlString = str(amFile.read())

    #show in terminal
    print('[+] Printing AndroidManifest.xml')
    print(xmlString.replace('\\n','\n'))

    # Let's go with static analysis
    print('[!] Maybe normal things...')
    if("ACCESS_NETWORK_STATE" in xmlString):
        print('\t[+] Mmm want to access ACCESS_NETWORK_STATE')
    if("ACCESS_WIFI_STATE" in xmlString):
        print('\t[+] Mmm want to access ACCESS_WIFI_STATE')
    if("CHANGE_WIFI_STATE" in xmlString):
        print('\t[+] Mmm want to access CHANGE_WIFI_STATE')

    print("%s"%WARNING)
    print('[!] Maybe some strange things...')
    if("CAMERA" in xmlString):
        print('\t[+] Mmm want to access CAMERA, look for NSA spy')
    if("hardware.camera" in xmlString):
        print('\t[+] Mmm just for devices with CAMERAAAA')
    if("READ_CONTACTS" in xmlString):
        print('\t[+] Mmm want to READ_CONTACTS, take a look')
    if("RECORD_AUDIO" in xmlString):
        print('\t[+] Mmm want to RECORD_AUDIO, I hope you must press a button for that')
    if("WRITE_SETTINGS" in xmlString):
        print('\t[+] Ohh Want to WRITE_SETTINGS,bad...bad...bad')
    print("%s"%ENDC)

    print("%s"%FAIL)
    print('[!] Ohh so strange things...')
    if("SEND_SMS" in xmlString):
        print('\t[+] Ohh want to SEND_SMS')
    if("RECEIVE_SMS" in xmlString):
        print('\t[+] Ohh want to RECEIVE_SMS look for receiver in code')
    if("READ_SMS" in xmlString):
        print('\t[+] Ohh want to READ_SMS look for receiver in code')
    if("WRITE_SMS" in xmlString):
        print('\t[+] Ohh want to WRITE_SMS')
    if("WRITE_CONTACTS" in xmlString):
        print('\t[+] Why want to WRITE_CONTACTS ?')
    if("CALL_PHONE" in xmlString):
        print('\t[+] Oh really? accept CALL_PHONE')
    if("PROCESS_OUTGOING_CALLS" in xmlString):
        print('\t[+] Mother of Edward Snowden, PROCESS_OUTGOING_CALLS O.O')
    if("KILL_BACKGROUND_PROCESSES" in xmlString):
        print('\t[+] KILL_BACKGROUND_PROCESSES, even Demi Lovato wouldn\'t accept this app ')
    print("%s"%ENDC)

    #close file
    amFile.close()
    #finally we return to directory 
    print('[+] Change directory to: '+actualDirectory)
    os.chdir(actualDirectory)

def readLibraries(directory): 
    '''
        Process to read library from android native libraries, discover
        Java functions and finally dissassembling it

        This extract Native code(arm,intel or mips).
    '''
    global WARNING
    global ENDC

    actualDirectory = os.getcwd() 

    print('[+] Change directory to: '+directory)
    os.chdir(directory)

    print('[+] Listing all native libraries')
    print('[+] It will show java class from those libraries')

    for root,dirs,files in os.walk('.'):
        for file in files:
            if file.endswith('.so'):
                pathFile = os.path.join(root,file)
                print(WARNING)
                print("[+] File: "+pathFile)
                print(ENDC)
                statement = 'objdump -T '+pathFile+' | grep Java_'
                os.system(statement)

                print("[+] Disassembling file in: "+file+".txt")
                if "arm" in pathFile: #for arm libs
                    statement = 'arm-linux-androideabi-objdump -d '+pathFile+' > '+file+'.txt'
                    os.system(statement)
                elif "86" in pathFile: #for x86 32 bits libs
                    statement = 'i686-linux-android-objdump -d '+pathFile+' > '+file+'.txt'
                    os.system(statement)
                elif "mips" in pathFile: #just for Rico's mind
                    statement = 'mipsellinux-android-objdump -d '+pathFile+' > '+file+'.txt'
                    os.system(statement)
                #end if
    print('[+] Returning to directory: '+actualDirectory)
    os.chdir(actualDirectory)

def readDatabases(directory):
    '''
        Extract schema from SQLite Database
    '''
    actualDirectory = os.getcwd() 

    print('[+] Let\'s going to read databases')
    print('[+] Change directory to: '+directory)
    os.chdir(directory)

    for root,dirs,files in os.walk('.'):
        for file in files:
            if file.endswith('.db') or file.endswith('.sqlite'):
                pathFile = os.path.join(root,file)

                print("[!] DataBase: "+pathFile)
                #create connection and execute sqlite queries
                con = sqlite3.connect(pathFile)
                cursor = con.cursor()
                tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                for table in tables:
                    print("\t[+] Table: "+table[0])
                    columns = cursor.execute("SELECT * FROM "+table[0]+";").description
                    for column in columns:
                        print("\t\t[+] Column: "+column[0])

    print('[+] Returning to directory: '+actualDirectory)
    os.chdir(actualDirectory)

###########################################################################

####################################UNZIP##################################
def unzipFunc(file):
    global outputName
    global regularExpresion

    print ("[+] Creating Directory from apk to unzip output...")
    actualDirectory = os.getcwd() #get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    #create name directory as: actualDirectory/apktool-outputName
    outputFile = actualDirectory + "/" + "unzip-" + outputName
    sentence = 'unzip '+file+' -d '+outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
        readCertificate(outputFile)
        input("[!] Press enter")
        listAsset(outputFile)
        input("[!] Press enter")
        listCode(outputFile)
        input("[!] Press enter")
        showStrings(outputFile,regularExpresion)
    except Exception as e:
        os.chdir(actualDirectory)
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need unzip...")

def listCode(directory):
    '''
        Module to list all possible code files
        now we will list .apk, .jar, .class
        from unzip content
    '''

    print('[+] Showing possible code files inside unzip project')
    statement = "find "+directory+" | grep \"apk\|jar\|class\" "
    os.system(statement)

def readCertificate(directory):
    '''
        Module to read the certificate from directory
        that unzip has created
    '''
    actualDirectory = os.getcwd() 

    
    print('[+] Change directory to: '+directory)
    os.chdir(directory)

    print('[+] Reading the application certificate...')
    statement = 'keytool -printcert -file ./META-INF/CERT.RSA'
    try:
        os.system(statement)
    except Exception as e:
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need keytool...")

    print('[+] Returning to Directory: '+actualDirectory)
    os.chdir(actualDirectory)

def listAsset(directory):
    '''
        Module to list assets directory (if exists)
    '''
    actualDirectory = os.getcwd()

    print('[+] Change directory to: '+directory)
    os.chdir(directory)

    print('[+] Looking for assets directory...')
    subdirs = os.listdir('.')

    if "assets" in subdirs:
        print('[+] Okey I think that we have assets file...')
        #show in a cool way
        for root,dirs,files in os.walk('./assets'):
            for file in files:
                print("[+] File assets: "+os.path.join(root,file))
    else:
        print('[+] There\'s no assets file')

    print("[+] Returning to Directory: "+actualDirectory)
    os.chdir(actualDirectory)

def showStrings(directory,regEx):
    '''
        Module to show strings from .dex file or
        files in general with some regular Expressions
    '''
    javaclassRegEx = '"L[^;]+?;"' #Objects or classes (start by L)
    urlRegEx = '"https?:"' #http or https
    urlBase64RegEx = '"aHR0cDo|aHR0cHM6L"' #http or https in base64

    actualDirectory = os.getcwd()

    print('[+] Change diretory to: '+directory)
    os.chdir(directory)

    for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.dex'):
                        print('[+] Showing strings for: '+os.path.join(root,file))
                        os.system("strings "+os.path.join(root,file)+" | egrep "+javaclassRegEx)
                        os.system("strings "+os.path.join(root,file)+" | egrep "+urlRegEx)
                        os.system("strings "+os.path.join(root,file)+" | egrep "+urlBase64RegEx)
                        if regEx != '':
                            os.system("strings "+os.path.join(root,file)+" | egrep "+regEx)
                    else:
                        print('[+] Showing strings for: '+os.path.join(root,file))
                        os.system("cat "+os.path.join(root,file)+" | egrep "+javaclassRegEx)
                        os.system("cat "+os.path.join(root,file)+" | egrep "+urlRegEx)
                        os.system("cat "+os.path.join(root,file)+" | egrep "+urlBase64RegEx)
                        if regEx != '':
                            os.system("cat "+os.path.join(root,file)+" | egrep "+regEx)

    print("[+] Returning to Directory: "+actualDirectory)
    os.chdir(actualDirectory)
###########################################################################

#################################FOR JADX##################################
def jadxFunc(file):
    global outputName

    print("[+] Creating directory from apk to jadx output...")
    actualDirectory = os.getcwd() #get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    #create name directory as: actualDirectory/apktool-outputName
    outputFile = actualDirectory + "/" + "jadx-" + outputName
    sentence = 'jadx-script '+' -d '+outputFile +" "+ file

    try:
        os.system(sentence)
        input("[!] Press enter")

        #show methods from files
        os.chdir(outputFile)
        for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.java'):
                        print('\t\t[+] SCANNING METHODS FROM: '+os.path.join(root,file))
                        os.system("cat "+os.path.join(root,file)+" | egrep "+'"(public|protected|private) .+\(*\)"')

    except Exception as e:
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need jadx-script (try to use install function)...")
    os.chdir(actualDirectory)

###################################FOR DEXDUMP#############################
import xml.etree.ElementTree as ET
import subprocess # for data from files
def opcodesFunc(file):
    global outputName

    print("[+] Creating files from apk to dexdump output...")
    actualDirectory = os.getcwd() #get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    print('[+] Creating opcodes file...')
    outputFile = actualDirectory + "/" + "opcode-" + outputName +".txt"
    sentence = 'dexdump '+' -d '+file + ' > '+outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
    except Exception as e:
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need dexdump...")

    print('[+] Creating headers file...')
    outputFile = actualDirectory + "/" + "summary-" + outputName +".txt"
    sentence = 'dexdump '+' -f '+file + ' > '+outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
    except Exception as e:
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need dexdump...")

    print('[+] Creating aditional informations about headers file...')
    outputFile = actualDirectory + "/" + "summaryDetails-" + outputName +".txt"
    sentence = 'dexdump '+' -f '+file + ' > '+outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
    except Exception as e:
        printDebug("[Debug] Error: "+str(e))
        print("[-] Maybe you need dexdump...")

    #### Now get receiver from androidManifest and Code
    # First from code
    ReceiverCode = list()

    command = "dexdump -i -l xml " + file
    output = subprocess.check_output(command, shell=True)
    xml = ET.fromstring(output)

    for node in xml.iter("class"): #iterate from all xml tree
        # Look for BroadcastReceiver
        if node.attrib["extends"]=="android.content.BroadcastReceiver":
            package = ""
            for child in node.iter("constructor"):
                package = child.attrib["type"]
            # for every BroadcastReceiver put into the list
            ReceiverCode.append(package + "." + node.attrib["name"])

    ReceiverAndroidManifest = list()    
    # Create "AndroidManifest.xml file"
    outputManifestFile = "/tmp/AndroidManifest.xml.tmp"
    
    print("[+] Using manifestDecoder")
    # Fixed problems to use with python3
    command = "manifestDecoder.py " + file
    os.system(command)

    command = "cat " + outputManifestFile + " | grep manifest | sed -nE 's/.*package=\"([^\"]+)\".*/\\1/p'"
    package = subprocess.check_output(command, shell=True)#.replace("\n", "")
    package = str(package).replace("\n","")

    command = "cat " + outputManifestFile + " | grep " + "receiver" + " | sed -nE 's/.*" + "name" + "=\"([^\"]+)\".*/\\1/p'"
    elements = subprocess.check_output(command, shell=True)
    elements = str(elements).split("\n")
    for element in elements:
        if element and element.strip():
            if(element.startswith(".")):
                ReceiverAndroidManifest.append(package + element)
            else:
                ReceiverAndroidManifest.append(element)

    os.remove(outputManifestFile)

    print('[+] Receivers in code from hexdump: ')
    for rc in ReceiverCode:
        print('\t[+] '+rc)
    print('[+] Receivers in AndroidManifest: ')
    for ra in ReceiverAndroidManifest:
        print('\t[+] '+ra)

    print('[+] Receivers that are in code but not in AndroidManifest: ')
    for rc in ReceiverCode:
        found = False
        for ra in ReceiverAndroidManifest:
            if (rc.startswith(ra)):
                found = True
                break
        if not found:
            print('\t[+] '+rc)

###################################For dex2jar#############################
def getjarFunc(file):
    '''
        Function to call dex2jar
    '''

    print ("[+] Creating Directory and jar from apk...")
    actualDirectory = os.getcwd() #get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)


    nameNoAPK = file.replace('.apk','') #name without .apk
    nameDEX2JAR = nameNoAPK + '_dex2jar.jar' #name from dex2jar output

    print("[+] Creating file "+nameDEX2JAR)
    sentence = 'dex2jar '+file
    os.system(sentence)

    print("[+] Creating folder "+nameNoAPK+'_CLASS and change directory')
    os.mkdir(nameNoAPK+'_CLASS')
    os.chdir(nameNoAPK+'_CLASS')

    print("[+] Creating classes files")
    sentence = 'unzip ../'+nameDEX2JAR
    os.system(sentence)

    print("[+] Returning to: "+actualDirectory)
    os.chdir(actualDirectory)

###################################To Create apk from apktool folder#######
def createAPKFunc(folder,apkName):

    print('[+] Creating temporary file before sign apk')
    sentence = 'apktool b '+folder+' -o changed_apk.apk'
    os.system(sentence)

    files = os.listdir('.')

    if 'changed_apk.apk' in files:
        print('[+] Creating signed apk')
        sentence = 'd2j-apk-sign -f -o '+apkName+' changed_apk.apk'
        os.system(sentence)
        print('[+] Removing temporary file')
        os.remove('changed_apk.apk')
        print('[+] Well now you can use your new apk')
    else:
        print('[-] There was a problem with apktool and temporary file')
###################################Exiftool################################
def extractMetaData(directory):
    '''
        Program to extract metadata from files
        .jpg,.png,.pdf,.csv,.txt...
    '''
    jpgFormat = False
    pngFormat = False
    pdfFormat = False
    csvFormat = False
    txtFormat = False

    actualDirectory = os.getcwd()

    print('[+] Change diretory to: '+directory)
    os.chdir(directory)

    print('[+] Now you will select files to extract metadata, \'y\' to select that extension, another one to refuse')

    if str(input('\t[+] JPG: ')).lower() == 'y':
        jpgFormat = True

    if str(input('\t[+] PNG: ')).lower() == 'y':
        pngFormat = True

    if str(input('\t[+] PDF: ')).lower() == 'y':
        pdfFormat = True

    if str(input('\t[+] CSV: ')).lower() == 'y':
        csvFormat = True

    if str(input('\t[+] TXT: ')).lower() == 'y':
        txtFormat = True

    try:
        if jpgFormat:
            for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.jpg'):
                        print("[+] Showing metadata for: "+os.path.join(root,file))
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if pngFormat:
            for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.png'):
                        print("[+] Showing metadata for: "+os.path.join(root,file))
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if pdfFormat:
            for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.pdf'):
                        print("[+] Showing metadata for: "+os.path.join(root,file))
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if csvFormat:
            for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.csv'):
                        print("[+] Showing metadata for: "+os.path.join(root,file))
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if txtFormat:
            for root,dirs,files in os.walk('.'):
                for file in files:
                    if file.endswith('.txt'):
                        print("[+] Showing metadata for: "+os.path.join(root,file))
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)
    except Exception as e:
        printDebug("Error: "+str(e))
        print('[-] Error, maybe you need exiftool')
    finally:
        print('[+] Returning to: '+actualDirectory)
        os.chdir(actualDirectory)


###########################################################################



def handler(signum,frame):
    global totalHelp
    print("Ohh don't like help print?")
    print (totalHelp)
    sys.exit(0)

def showTotalHelp():
    global totalHelp
    signal.signal(signal.SIGINT,handler)
    print("Press CTRL-C to skip")
    for c in totalHelp:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.25)

def main():
    
    global outputName
    global apkFile
    global apktoolUse
    global unzipUse
    global exiftoolUse
    global regularExpresion
    global jadxUse
    global opcodesUse
    global allReal 
    global getjar
    global createAPK
    global folderWithCode
    global apkOutputName
    
    

    help = '''
        ./androidSwissKnife.py [--install] [--man] -a <apk_file> -o <output_directories_name> [--apktool] [--unzip] [--regEx <"regular Expression">] [--exiftool] [--jadx] [--opcodes] [--all] [--create-apk -f <folder from apktool> -apk <name for apk>]
        --install: To install some necessary tools
        -a:     apk file in your directory or absolute path
        -o:     Name for output directories
        --apktool:  use apktool in Analysis
        --unzip: use unzip in Analysis
        --regEx: with unzip function we use a strings searching, you can add a regular Expression (by default URLs and Java Classes)
        --exiftool: use exiftool with some file formats (you need first --apktool)
        --jadx: use jadx to try to get source code
        --opcodes: Get information from opcodes
        --get-jar: Get jar from apk and finally the .class in a folder
        --all: use all Analysis
        --create-apk: generate an apk, from apktool folder
        --man: get all the help from the program as star wars film

        Ejemplo:    ./androidSwissKnife.py -a dragonForce.apk -o analysis_dragon --apktool
    '''
    for index in range(len(sys.argv)):
        if sys.argv[index] == '--install':
            install()
            sys.exit(0)
        if sys.argv[index] == '--man':
            showTotalHelp()
            sys.exit(0)
        if sys.argv[index] == '-a':
            apkFile = str(sys.argv[index+1])
        if sys.argv[index] == '-o':
            outputName = str(sys.argv[index+1])
        if sys.argv[index] == '--apktool':
            apktoolUse = True
        if sys.argv[index] == '--unzip':
            unzipUse = True
        if sys.argv[index] == '--exiftool':
            exiftoolUse = True
        if sys.argv[index] == '--regEx':
            regularExpresion = sys.argv[index+1]
        if sys.argv[index] == '--jadx':
            jadxUse = True
        if sys.argv[index] == '--opcodes':
            opcodesUse = True
        if sys.argv[index] == '--get-jar':
            getjar = True
        if sys.argv[index] == '--create-apk':
            createAPK = True
        if sys.argv[index] == '-f':
            folderWithCode = str(sys.argv[index+1])
        if sys.argv[index] == '-apk':
            apkOutputName = str(sys.argv[index+1])
        if sys.argv[index] == '--all':
            allReal = True
            exiftoolUse = True

    if (not createAPK) and (not apktoolUse) and (not unzipUse) and (not exiftoolUse) and (not jadxUse) and (not opcodesUse) and (not getjar )and (not allReal):
        print(help)
        sys.exit(0)


    if createAPK:
        if (folderWithCode == '' ) or (apkOutputName == ''):
            print(help)
            sys.exit(0)
        createAPKFunc(folderWithCode,apkOutputName)
            
    if allReal:
        if apkFile == '':
            print(help)
            sys.exit(0)
        if outputName == '':
            print(help)
            sys.exit(0)

        createApktoolFunc(apkFile)
        unzipFunc(apkFile)
        jadxFunc(apkFile)
        opcodesFunc(apkFile)
        getjarFunc(apkFile)
    else:
        if apkFile == '':
            print(help)
            sys.exit(0)
        if outputName == '':
            print(help)
            sys.exit(0)
        if apktoolUse:
            createApktoolFunc(apkFile)
        if unzipUse:
            unzipFunc(apkFile)
        if jadxUse:
            jadxFunc(apkFile)
        if opcodesUse:
            opcodesFunc(apkFile)
        if getjar:
            getjarFunc(apkFile)

if __name__ == "__main__":
    print(random.choice(bannerP))
    time.sleep(2)
    print (banner)
    time.sleep(1)
    main()
