#!/usr/bin/env python3

'''
    
    Application to use with APK to create
    files for Static analysis.

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

# about me and program
programmer = "Fare9"
version = 3.0

# banner
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

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

secAdmin = '''
                     _______. _______   ______ 
                    /       ||   ____| /      |
                   |   (----`|  |__   |  ,----'
                    \   \    |   __|  |  |     
                .----)   |   |  |____ |  `----.
                |_______/    |_______| \______|

.______________________________________________________|_._._._._._._._._._.
 \_____________________________________________________|_#_#_#_#_#_#_#_#_#_|
                                                       l
             ___       _______  .___  ___.  __  .__   __. 
            /   \     |       \ |   \/   | |  | |  \ |  | 
           /  ^  \    |  .--.  ||  \  /  | |  | |   \|  | 
          /  /_\  \   |  |  |  ||  |\/|  | |  | |  . `  | 
         /  _____  \  |  '--'  ||  |  |  | |  | |  |\   | 
        /__/     \__\ |_______/ |__|  |__| |__| |__| \__| 
'''

ciberSeg = '''
  ______  __  .______    _______ .______          _______. _______   _______
 /      ||  | |   _  \  |   ____||   _  \        /       ||   ____| /  _____|
|  ,----'|  | |  |_)  | |  |__   |  |_)  |      |   (----`|  |__   |  |  __
|  |     |  | |   _  <  |   __|  |      /        \   \    |   __|  |  | |_ |
|  `----.|  | |  |_)  | |  |____ |  |\  \----.----)   |   |  |____ |  |__| |
 \______||__| |______/  |_______|| _| `._____|_______/    |_______| \______|

                __    __       ___       __    __
               |  |  |  |     /   \     |  |  |  |
               |  |  |  |    /  ^  \    |  |__|  |
               |  |  |  |   /  /_\  \   |   __   |
               |  `--'  |  /  _____  \  |  |  |  |
                \______/  /__/     \__\ |__|  |__|
'''

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
''' % (WARNING, ENDC, WARNING, ENDC, WARNING, ENDC, WARNING, ENDC, FAIL, ENDC, WARNING, ENDC, str(version), programmer)




############################ END OF BANNER
try:
  import os  # to use operating system commands
  import sys
  import time
  import random
  import signal
  import sqlite3
  import pprint
  import json  # to load logs from logcat
  import codecs
  import argparse # set new parsing forms
  import magic # get mimetype

  # My own classes
  import adbClass
  from supportClasses.koodous import *
  from supportClasses.utilities import *
  from supportClasses.permissions import *
  from supportClasses.filters import *
except Exception as e:
  print ("[-] You have problems with one library: "+str(e))
####################################
# global variables for input

## Information from apk, will be a dictionary, we can get it 
## when finish analysis as output
apkInformation = {}


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
## Dynamic analysis just will be dynamic analysis...
DynamicAnalysis = False
## Koodous antivirus analysis
koodousAnalysis = False
uploadKoodous = False
# variable for debugging
debug = True

totalHelp = '''
All help is here...

First use: --apktool

We will use apktool to extract data compressed in your apk, please install
the last version of apktool.
When finished the process of descompressing with apktool, we will read the
AndroidManifest.xml and show some strange data (or not) now implemented
permissions and filters.
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

###### NEW FEATURES ########
--create-apk
Once you have used apktool to get smali code from an apk, you can modify it, and finally
create another apk with your changes, you can use this feature to do it.

### FINALLY DYNAMIC ANALYSIS (DroidBox Wrapper)
--DroidBox (Original Idea https://github.com/pjlantz/droidbox/tree/master/droidbox4.1.1)
I modified DroidBox code to this framework, I rewrite some functions to work in python3
but nothing change from this program. You need to have an android emulator, in Readme.md
you can see the features of my emulator.


### Koodous extension ###
--Koodous
Try to quick analyze your apk with koodous the antivirus from community.
https://koodous.com
If exists the apk, you will get quick analysis

--upload
If you want to upload your APK to Koodous to analyze.
'''




###################################### Some usefull functions


def printDebug(string):
    global debug
    if debug:
        print (string)


def install():
    '''
        Function to help the work of installing androidSwissKnife, maybe It's not perfect
        but you can take step by step manually
    '''

    if os.geteuid() != 0:
        print("[-] You need to be root to install packages")
        exit(-1)

    os.mkdir("Tools")

    actualDirectory = os.getcwd()

    print("[+] Creating symbolic links for androidSwissKnife")

    # link actual directory to variable path (directory where you have androidSwissKnife)
    os.system("echo PATH=\$PATH:" + actualDirectory + " >> ~/.bashrc")

    # add permissions to exec
    os.system("chmod +x $PWD/androidSwissKnife.py")
    os.system("chmod +x $PWD/manifestDecoder.py")

    print("[+] Now you can call the tool anywhere with: androidSwissKnife.py")
    print("[+] Going to Directory Tools")
    os.chdir("Tools")

    print("[+] Installing last version of apktool")
    os.system("wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.2.2.jar")

    os.system("chmod +x ./apktool_2.2.2.jar")

    os.system("ln -sf $PWD/apktool_2.2.2.jar /usr/bin/apktool")

    print("[+] Installing last version of jadx")

    os.system("git clone https://github.com/skylot/jadx.git")
    os.chdir("jadx")

    os.system("./gradlew dist")
    os.system("ln -s $PWD/build/jadx/bin/jadx /usr/bin/jadx")
    os.system("ln -s $PWD/build/jadx/bin/jadx-gui /usr/bin/jadx-gui")

    os.chdir("..")  # Go to Tools
    print("[+] Installing exiftool")
    os.system("sudo apt-get install exiftool")

    print("[+] Installing unzip (if you don't have it yet)")
    os.system("sudo apt-get install unzip")

    print('[+] Installing pip3 ')
    os.system("sudo apt-get install python3-pip")

    print('[+] Installing libraries')
    os.system("pip3 install bytecode")
    os.system("pip3 install python-magic")
    os.system("sudo apt-get install lib32z1 lib32stdc++6")

    print("[!] Please Install at your own Android SDK and NDK from Android webpage")
    print("\t[+] Then add bin and tools folders from  sdk and ndk to the variable PATH in .bashrc")

    example = '''
    PATH=$PATH:/usr/local/android-studio/bin
    PATH=$PATH:/usr/local/android-ndk-r12b/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin
    PATH=$PATH:/usr/local/android-ndk-r12b/toolchains/x86-4.9/prebuilt/linux-x86_64/bin
    PATH=$PATH:/usr/local/android-ndk-r12b/toolchains/mipsel-linux-android-4.9/prebuilt/linux-x86_64/bin
    PATH=$PATH:/root/Android/Sdk/tools
    PATH=$PATH:/root/Android/Sdk/platform-tools
    PATH=$PATH:/root/Android/Sdk/build-tools/24.0.0
    '''
    print("\t[+] Here an example to add to your .bashrc file: \n" + example)

    print("###################################################")
    print("\n\n\tFor Dynamic Analysis:")
    print("Once you've got Android Studio, you can add SmaliIdea for smali support")
    print("Open Android Studio, go to Settings->Plugins and click \"Install plugin from disk\"")
    print("And install Smalidea zip from androidSwissKnife folder, then click Apply")
    print("Smalidea from JesusFreke: https://github.com/JesusFreke")
    print("Install Burpsuite")
    print("Create an android emulator")
    print("[+] Installing BeautifulSoup")
    os.system("pip3 install bs4")
    print("[+] Returning to: " + actualDirectory)


##################################### START ALWAYS ANALYSIS #########################
def checkFile(file):
    '''
        module to get information from the apk: filetype and 
        hashes
    '''
    global apkInformation

    # first put filename in apkInformation
    apkInformation['file_name'] = file
    print("[+] File: "+str(file))
    # get mymetype and add it to apkInformation
    print("[+] Getting mime type...")
    mimetype = magic.from_file(file, mime=True)
    apkInformation['mime_type'] = str(mimetype)
    print("[+] Mime type: "+str(mimetype))

    # get hashes
    print("[+] Getting hashes...")
    hashing = adbClass.DynamicAnalyzer(apk=file)
    md5,sha1,sha256 = hashing.getHash()
    print("\t[!] MD5: "+str(md5))
    print("\t[!] SHA1: "+str(sha1))
    print("\t[!] SHA256: "+str(sha256))
    apkInformation['md5'] = str(md5)
    apkInformation['sha1'] = str(sha1)
    apkInformation['sha256'] = str(sha256)



##################################### FOR APKTOOL ###################################
def createApktoolFunc(file):
    '''
        Module to get directory with apk resolution
        from apktool, well we need apktool
    '''

    global outputName
    global exiftoolUse

    print ("[+] Creating Directory from apk to apktool output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    # create name directory as: actualDirectory/apktool-outputName
    outputFile = actualDirectory + "/" + "apktool-" + outputName
    sentence = 'apktool d ' + file + ' -o ' + outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
        readAndroidManifest(outputFile)
        input("[!] Press enter")
        readInterestingFilters(outputFile)
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
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need apktool...")


def readAndroidManifest(directory):
    '''
        Module to read AndroidManifest we will add some 
        features from static analysis

        Please add what you want if you thing something is strange
    '''
    global apkInformation
    apkInformation['permissions'] = {}
    global WARNING
    global FAIL
    global ENDC
    actualDirectory = os.getcwd()  # to return after analysis of AndroidManifest

    # change to apktool directory and read AndroidManifest.xml
    print('[+] Change directory to: ' + directory)
    os.chdir(directory)

    amFile = open('AndroidManifest.xml', 'rb')
    xmlString = str(amFile.read())

    # show in terminal
    print('[+] Printing AndroidManifest.xml')
    print(xmlString.replace('\\n', '\n'))

    # Let's go with static analysis
    print('[!] Maybe normal things...')
    apkInformation['permissions']['Normal_Things'] = []
    for key in normal_things:
        if key in xmlString:
            apkInformation['permissions']['Normal_Things'].append(key)
            print(normal_things[key])

    print("%s" % WARNING)
    print('[!] Maybe some strange things...')
    apkInformation['permissions']['Strange_Things'] = []
    for key in strange_things:
        if key in xmlString:
            apkInformation['permissions']['Strange_Things'].append(key)
            print(strange_things[key])
    print("%s" % ENDC)

    print("%s" % FAIL)
    print('[!] Ohh so strange things...')
    apkInformation['permissions']['Problem_Things'] = []
    for key in problem_things:
        if key in xmlString:
            apkInformation['permissions']['Problem_Things'].append(key)
            print(problem_things[key])
    print("%s" % ENDC)

    # close file
    amFile.close()
    # finally we return to directory
    print('[+] Change directory to: ' + actualDirectory)
    os.chdir(actualDirectory)


def readInterestingFilters(directory):
    '''

    :param directory:
    :return:
    '''
    global apkInformation
    apkInformation['Filters'] = []

    global WARNING
    global FAIL
    global ENDC
    actualDirectory = os.getcwd()  # to return after analysis of AndroidManifest

    # change to apktool directory and read AndroidManifest.xml
    print('[+] Change directory to: ' + directory)
    os.chdir(directory)

    amFile = open('AndroidManifest.xml', 'rb')
    xmlString = str(amFile.read())
    print("[+] Let's going to look for interesting filters")

    print('[+] Stranger filters: ')
    for key in filterString:
        if key in xmlString:
            apkInformation['Filters'].append(key)
            print(filterString[key])

    # close file
    amFile.close()
    # finally we return to directory
    print('[+] Change directory to: ' + actualDirectory)
    os.chdir(actualDirectory)


def readLibraries(directory):
    '''
        Process to read library from android native libraries, discover
        Java functions and finally dissassembling it

        This extract Native code(arm,intel or mips).
    '''
    global apkInformation
    apkInformation['Native_Methods'] = []

    global WARNING
    global ENDC

    actualDirectory = os.getcwd()

    print('[+] Change directory to: ' + directory)
    os.chdir(directory)

    print('[+] Listing all native libraries')
    print('[+] It will show java class from those libraries')

    for root, dirs, files in os.walk('.'):
        for file in files:
            try:
                if file.endswith('.so'):  # If it is .so file (native library)
                    pathFile = os.path.join(root, file)
                    print(WARNING)
                    print("[+] File: " + pathFile)
                    print(ENDC)
                    statement = 'objdump -T ' + pathFile + ' | grep Java_'  # we use objdump to show strings then find Java functions
                    # os.system(statement)
                    error = False
                    try:
                        output = subprocess.check_output(statement, shell=True)
                    except subprocess.CalledProcessError as e:
                        print("[-] Error in objdump: " + str(e))
                        error = True

                    if error:
                        print(output)
                    else:
                        native_methods = parseObjDump(output,pathFile)
                        pprint.pprint(native_methods)
                        apkInformation['Native_Methods'].append(native_methods)

                    print("[+] Disassembling file in: " + file + ".txt")
                    if "arm" in pathFile:  # for arm libs
                        statement = 'arm-linux-androideabi-objdump -d ' + pathFile + ' > ' + file + '.txt'
                        os.system(statement)
                    elif "86" in pathFile:  # for x86 32 bits libs
                        statement = 'i686-linux-android-objdump -d ' + pathFile + ' > ' + file + '.txt'
                        os.system(statement)
                    elif "mips" in pathFile:  # just for Rico's mind
                        statement = 'mipsel-linux-android-objdump -d ' + pathFile + ' > ' + file + '.txt'
                        os.system(statement)
                        # end if
            except: #maybe not Java functions
                continue
    print('[+] Returning to directory: ' + actualDirectory)
    os.chdir(actualDirectory)


def readDatabases(directory):
    '''
        Extract schema from SQLite Database
    '''
    actualDirectory = os.getcwd()

    print('[+] Let\'s going to read databases')
    print('[+] Change directory to: ' + directory)
    os.chdir(directory)

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.db') or file.endswith('.sqlite'):
                pathFile = os.path.join(root, file)

                print("[!] DataBase: " + pathFile)
                # create connection and execute sqlite queries
                con = sqlite3.connect(pathFile)
                cursor = con.cursor()
                tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                for table in tables:
                    print("\t[+] Table: " + table[0])
                    columns = cursor.execute("SELECT * FROM " + table[0] + ";").description
                    for column in columns:
                        print("\t\t[+] Column: " + column[0])

    print('[+] Returning to directory: ' + actualDirectory)
    os.chdir(actualDirectory)


###########################################################################

####################################UNZIP##################################
def unzipFunc(file):
    '''
        Unzip apk to unzip folder, then use this folder for other functions
    '''
    global outputName
    global regularExpresion

    print ("[+] Creating Directory from apk to unzip output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    # create name directory as: actualDirectory/unzip-outputName
    outputFile = actualDirectory + "/" + "unzip-" + outputName
    sentence = 'unzip ' + file + ' -d ' + outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
        readCertificate(outputFile)
        input("[!] Press enter")
        listAsset(outputFile)
        input("[!] Press enter")
        listCode(outputFile)
        input("[!] Press enter")
        showStrings(outputFile, regularExpresion)
    except Exception as e:
        os.chdir(actualDirectory)
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need unzip...")


def listCode(directory):
    '''
        Module to list all possible code files
        now we will list .apk, .jar, .class
        from unzip content
    '''

    print('[+] Showing possible code files inside unzip project')
    statement = "find " + directory + " | grep \"apk\|jar\|class\" "
    os.system(statement)


def readCertificate(directory):
    '''
        Module to read the certificate from directory
        that unzip has created
    '''
    actualDirectory = os.getcwd()

    print('[+] Change directory to: ' + directory)
    os.chdir(directory)

    print('[+] Reading the application certificate...')
    statement = 'keytool -printcert -file ./META-INF/CERT.RSA'
    try:
        os.system(statement)
    except Exception as e:
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need keytool...")

    print('[+] Returning to Directory: ' + actualDirectory)
    os.chdir(actualDirectory)


def listAsset(directory):
    '''
        Module to list assets directory (if exists)
        maybe you can find interesting files
    '''
    actualDirectory = os.getcwd()

    print('[+] Change directory to: ' + directory)
    os.chdir(directory)

    print('[+] Looking for assets directory...')
    subdirs = os.listdir('.')

    if "assets" in subdirs:
        print('[+] Okey I think that we have assets file...')
        # show in a cool way
        for root, dirs, files in os.walk('./assets'):
            for file in files:
                print("[+] File assets: " + os.path.join(root, file))
    else:
        print('[+] There\'s no assets file')

    print("[+] Returning to Directory: " + actualDirectory)
    os.chdir(actualDirectory)


def showStrings(directory, regEx):
    '''
        Module to show strings from .dex file or
        files in general with some regular Expressions
    '''

    javaclassRegEx = '"L[^;]+?;"'  # Objects or classes (start by L in smali code)
    urlRegEx = '"https?:"'  # http or https
    urlBase64RegEx = '"aHR0cDo|aHR0cHM6L"'  # http or https in base64
    emails = '"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]"' # look for emails in code
    actualDirectory = os.getcwd()

    print('[+] Change diretory to: ' + directory)
    os.chdir(directory)

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.dex'): # for compiled files
                print('[+] Showing strings for: ' + os.path.join(root, file))
                os.system("strings " + os.path.join(root, file) + " | egrep " + javaclassRegEx)
                os.system("strings " + os.path.join(root, file) + " | egrep " + urlRegEx)
                os.system("strings " + os.path.join(root, file) + " | egrep " + urlBase64RegEx)
                os.system("strings " + os.path.join(root, file) + " | egrep " + emails)
                if regEx != '':
                    os.system("strings " + os.path.join(root, file) + " | egrep " + regEx)
            else: # another files
                print('[+] Showing strings for: ' + os.path.join(root, file))
                os.system("cat " + os.path.join(root, file) + " | egrep " + javaclassRegEx)
                os.system("cat " + os.path.join(root, file) + " | egrep " + urlRegEx)
                os.system("cat " + os.path.join(root, file) + " | egrep " + urlBase64RegEx)
                os.system("cat " + os.path.join(root, file) + " | egrep " + emails)
                if regEx != '':
                    os.system("cat " + os.path.join(root, file) + " | egrep " + regEx)

    print("[+] Returning to Directory: " + actualDirectory)
    os.chdir(actualDirectory)


###########################################################################

#################################FOR JADX##################################
def jadxFunc(file):
    '''
        Get Java code with jadx, It is not the best way, but is the prettiest
    '''
    global outputName

    print("[+] Creating directory from apk to jadx output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    # create name directory as: actualDirectory/jadx-outputName
    outputFile = actualDirectory + "/" + "jadx-" + outputName
    sentence = 'jadx ' + ' -d ' + outputFile + " " + file

    try:
        os.system(sentence)
        input("[!] Press enter")

        # show methods from files
        os.chdir(outputFile)
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.java'):
                    print('\t\t[+] SCANNING METHODS FROM: ' + os.path.join(root, file))
                    os.system("cat " + os.path.join(root, file) + " | egrep " + '"(public|protected|private) .+\(*\)"')

    except Exception as e:
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need jadx (try to use install function)...")
    os.chdir(actualDirectory)


###################################FOR DEXDUMP#############################
import xml.etree.ElementTree as ET
import subprocess  # for data from files


def opcodesFunc(file):
    global outputName

    print("[+] Creating files from apk to dexdump output...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    print('[+] Creating opcodes file...')
    outputFile = actualDirectory + "/" + "opcode-" + outputName + ".txt"
    sentence = 'dexdump ' + ' -d ' + file + ' > ' + outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
    except Exception as e:
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need dexdump...")

    print('[+] Creating headers file...')
    outputFile = actualDirectory + "/" + "summary-" + outputName + ".txt"
    sentence = 'dexdump ' + ' -f ' + file + ' > ' + outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
    except Exception as e:
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need dexdump...")

    print('[+] Creating aditional informations about headers file...')
    outputFile = actualDirectory + "/" + "summaryDetails-" + outputName + ".txt"
    sentence = 'dexdump ' + ' -f ' + file + ' > ' + outputFile

    try:
        os.system(sentence)
        input("[!] Press enter")
    except Exception as e:
        printDebug("[Debug] Error: " + str(e))
        print("[-] Maybe you need dexdump...")

    #### Now get receiver from androidManifest and Code
    # First from code
    ReceiverCode = list()

    command = "dexdump -i -l xml " + file
    output = subprocess.check_output(command, shell=True)
    xml = ET.fromstring(output)

    for node in xml.iter("class"):  # iterate from all xml tree
        # Look for BroadcastReceiver
        if node.attrib["extends"] == "android.content.BroadcastReceiver":
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
    package = subprocess.check_output(command, shell=True)  # .replace("\n", "")
    package = str(package).replace("\n", "")

    command = "cat " + outputManifestFile + " | grep " + "receiver" + " | sed -nE 's/.*" + "name" + "=\"([^\"]+)\".*/\\1/p'"
    elements = subprocess.check_output(command, shell=True)
    elements = str(elements).split("\n")
    for element in elements:
        if element and element.strip():
            if (element.startswith(".")):
                ReceiverAndroidManifest.append(package + element)
            else:
                ReceiverAndroidManifest.append(element)

    os.remove(outputManifestFile)

    print('[+] Receivers in code from hexdump: ')
    for rc in ReceiverCode:
        print('\t[+] ' + rc)
    print('[+] Receivers in AndroidManifest: ')
    for ra in ReceiverAndroidManifest:
        print('\t[+] ' + ra)

    print('[+] Receivers that are in code but not in AndroidManifest: ')
    for rc in ReceiverCode:
        found = False
        for ra in ReceiverAndroidManifest:
            if (rc.startswith(ra)):
                found = True
                break
        if not found:
            print('\t[+] ' + rc)


###################################For dex2jar#############################
def getjarFunc(file):
    '''
        Function to call dex2jar, then you can see the code
        with others tools
    '''

    print ("[+] Creating Directory and jar from apk...")
    actualDirectory = os.getcwd()  # get actual directory

    # First take a look if path is relative or absolute
    isRelative = os.path.isabs(file)

    if isRelative:
        # if relative, well get absolute path
        file = os.path.abspath(file)

    nameNoAPK = file.replace('.apk', '')  # name without .apk
    nameDEX2JAR = nameNoAPK + '_dex2jar.jar'  # name from dex2jar output

    print("[+] Creating file " + nameDEX2JAR)
    sentence = 'dex2jar ' + file
    os.system(sentence)

    print("[+] Creating folder " + nameNoAPK + '_CLASS and change directory')
    os.mkdir(nameNoAPK + '_CLASS')
    os.chdir(nameNoAPK + '_CLASS')

    print("[+] Creating classes files")
    sentence = 'unzip ../' + nameDEX2JAR
    os.system(sentence)

    print("[+] Returning to: " + actualDirectory)
    os.chdir(actualDirectory)


###################################To Create apk from apktool folder#######
def createAPKFunc(folder, apkName):
    '''
        If you change smali code from apktool output, you can pack again
        in apk file with this function
    '''
    print('[+] Creating temporary file before sign apk')
    sentence = 'apktool b ' + folder + ' -o changed_apk.apk'
    os.system(sentence)

    files = os.listdir('.')

    if 'changed_apk.apk' in files:
        print('[+] Creating signed apk')
        sentence = 'd2j-apk-sign -f -o ' + apkName + ' changed_apk.apk'
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
    xmlFormat = False

    actualDirectory = os.getcwd()

    print('[+] Change diretory to: ' + directory)
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

    if str(input('\t[+] XML: ')).lower() == 'y':
        xmlFormat = True

    try:
        if jpgFormat:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.jpg'):
                        print("[+] Showing metadata for: " + os.path.join(root, file))
                        statement = 'exiftool ' + os.path.join(root, file)
                        os.system(statement)
                        time.sleep(0.5)

        if pngFormat:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.png'):
                        print("[+] Showing metadata for: " + os.path.join(root, file))
                        statement = 'exiftool ' + os.path.join(root, file)
                        os.system(statement)
                        time.sleep(0.5)

        if pdfFormat:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.pdf'):
                        print("[+] Showing metadata for: " + os.path.join(root, file))
                        statement = 'exiftool ' + os.path.join(root, file)
                        os.system(statement)
                        time.sleep(0.5)

        if csvFormat:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.csv'):
                        print("[+] Showing metadata for: " + os.path.join(root, file))
                        statement = 'exiftool ' + os.path.join(root, file)
                        os.system(statement)
                        time.sleep(0.5)

        if txtFormat:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.txt'):
                        print("[+] Showing metadata for: " + os.path.join(root, file))
                        statement = 'exiftool ' + os.path.join(root, file)
                        os.system(statement)
                        time.sleep(0.5)

        if xmlFormat:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.xml'):
                        print("[+] Showing metadata for: " + os.path.join(root, file))
                        statement = 'exiftool ' + os.path.join(root, file)
                        os.system(statement)
                        time.sleep(0.5)

    except Exception as e:
        printDebug("Error: " + str(e))
        print('[-] Error, maybe you need exiftool')
    finally:
        print('[+] Returning to: ' + actualDirectory)
        os.chdir(actualDirectory)


###########################################################################



def handler(signum, frame):
    global totalHelp
    print("Ohh don't like help print?")
    print (totalHelp)
    sys.exit(0)


def showTotalHelp():
    global totalHelp
    signal.signal(signal.SIGINT, handler)
    print("Press CTRL-C to skip")
    for c in totalHelp:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.05)


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
    global DynamicAnalysis
    global koodousAnalysis
    global uploadKoodous

    parser = argparse.ArgumentParser(description="AndroidSwissKnife application to help in apk analysis")
    parser.add_argument("--install",action="store_true",help="To install some necessary tools")
    parser.add_argument("-a","--apk",type=str,help="apk file in your directory or absolute path")
    parser.add_argument("-o","--output",type=str,help="Name for output directories")
    parser.add_argument("--apktool",action="store_true",help="use apktool in Analysis")
    parser.add_argument("--unzip",action="store_true",help="use unzip in Analysis")
    parser.add_argument("--regEx",type=str,help='with unzip function we use a strings searching, you can add a regular Expression (by default URLs and Java Classes)')
    parser.add_argument("--exiftool",action="store_true",help="use exiftool with some file formats (you need first --apktool)")
    parser.add_argument("--jadx",action="store_true",help="use jadx to try to get source code")
    parser.add_argument("--opcodes",action="store_true",help="Get information from opcodes")
    parser.add_argument("--get-jar",action="store_true",help="Get jar from apk and finally the .class in a folder")
    parser.add_argument("--all",action="store_true",help="use all Analysis")
    parser.add_argument("--create-apk",action="store_true",help="generate an apk, from apktool folder")
    parser.add_argument("--man",action="store_true",help="Get all the help from the program as star wars film")
    parser.add_argument("--DroidBox",action="store_true",help="New feature to do a dynamic analysis of the apk (It's a \"wrapper\" of droidbox with Burpsuite)")
    parser.add_argument("--Koodous",action="store_true",help="Try to search your apk in Koodous, it will take some time")
    parser.add_argument("--upload",action="store_true",help="If APK is not in koodous upload to analysis")
    parser.add_argument("-f","--folder",type=str,help='folder from apktool (needs --create-apk)')
    parser.add_argument("--apk-output",type=str,help='Output apk (needs --create-apk)')
    args = parser.parse_args()


    if args.install: # install androidswissknife
        install()
        sys.exit(0)
    if args.man: # show all the help
        showTotalHelp()
        sys.exit(0)
    if args.apk is not None: # get apkfile
        apkFile = str(args.apk)
    if args.output is not None:
        outputName = str(args.output)

    apktoolUse = args.apktool
    unzipUse = args.unzip
    exiftoolUse = args.exiftool

    if args.regEx is not None:
        regularExpresion = args.regEx

    jadxUse = args.jadx
    opcodesUse = args.opcodes
    getjar = args.get_jar
    createAPK = args.create_apk

    if args.folder is not None:
        folderWithCode = str(args.folder)
    if args.apk_output is not None:
        apkOutputName = str(args.apk_output)

    if args.all: # we do this in this way to set two options
        allReal = True
        exiftoolUse = True

    DynamicAnalysis = args.DroidBox
    koodousAnalysis = args.Koodous
    
    if (not koodousAnalysis) and (not createAPK) and (not apktoolUse) and (not unzipUse) and (
            not exiftoolUse) and (not jadxUse) and (not opcodesUse) and (not getjar) and (not allReal) and (
            not DynamicAnalysis):
        print("[-] Use --help or -h to check help")
        sys.exit(0)


    if apkFile != '':
        checkFile(apkFile) # always do this check if exists apk
        input()
    ##################################### Do a quick analysis with koodous, you need to write your token
    if koodousAnalysis:
        if apkFile == '':
            print(help)
            sys.exit(0)

        # First take a look if path is relative or absolute
        isAbs = os.path.isabs(apkFile)

        if not isAbs:
            # if relative, well get absolute path
            apkFile = os.path.abspath(apkFile)

        koodous = KoodousAnalyzer(apk=apkFile,upload=args.upload)
        koodous.analyzeApk()
        pprint.pprint(koodous.jsonOutput, indent=4)
        sys.exit(0)
    ##################################### Create an apk from apktool modification smali code
    if createAPK:
        if (folderWithCode == '') or (apkOutputName == ''):
            print(help)
            sys.exit(0)
        createAPKFunc(folderWithCode, apkOutputName)
        sys.exit(0)

    ##################################### Dynamic Anaylisis function with all necessary classes

    # Variables to save data from analysis
    sendsms = {}
    phonecalls = {}
    cryptousage = {}
    dexclass = {}
    dataleaks = {}
    opennet = {}
    sendnet = {}
    recvnet = {}
    closenet = {}
    fdaccess = {}
    servicestart = {}
    accessedfiles = {}
    errors = []  # If some line get an error, why don't we show it?

    if DynamicAnalysis:
        if apkFile == '':
            print(help)
            sys.exit(0)

        # First take a look if path is relative or absolute
        isAbs = os.path.isabs(apkFile)

        if not isAbs:
            # if relative, well get absolute path
            apkFile = os.path.abspath(apkFile)

        # start burpsuite
        prox = adbClass.Proxy()
        response = ''
        while ((response != 'y') and (response != 'n')):
            response = input("[+] Do you want to use Burpsuite? (Y/N): ")
            try:
                response = response.lower()
            except:
                print("[-] Please respond 'Y' or 'N'")
                continue

        if response == 'y':
            prox.startBurp()
            print(OKGREEN)
            adbClass.progressBar()
            print(ENDC)

        emulatorName = input("[+] Give me the emulator name: ")

        # create adb class
        adbHandler = adbClass.Adb(emulator=emulatorName, proxy=prox)

        # depends if you want burp proxy or not
        if response == 'n':
            adbHandler.startEmulator()
        elif response == 'y':
            adbHandler.startEmulatorProxy()

        # create DynamicAnalyzer class
        dynamicAnalizer = adbClass.DynamicAnalyzer(apk=apkFile)
        dynamicAnalizer.extractingApk()

        hashes = dynamicAnalizer.getHash()
        md5 = hashes[0]
        sha1 = hashes[1]
        sha256 = hashes[2]

        print("\n\n\n")
        print(WARNING)
        print("[+] Name of application: " + apkFile)
        print("[+] MD5: " + str(md5))
        print("[+] SHA1: " + str(sha1))
        print("[+] SHA256: " + str(sha256))
        print(ENDC)
        time.sleep(1)
        print(OKBLUE)
        print("################# DYNAMIC ANALYSIS #########################")
        print(ENDC)

        activities = dynamicAnalizer.activities
        mainActivity = dynamicAnalizer.mainActivity
        packages = dynamicAnalizer.packages
        if len(packages) > 0:
            packages = packages[0]
        usesPermissions = dynamicAnalizer.permissions
        permissions = dynamicAnalizer.outPermissions
        receivers = dynamicAnalizer.receivers
        recvsactions = dynamicAnalizer.recvsactions
        print("[+] MainActivity: " + str(mainActivity))
        time.sleep(1)
        print("[+] Activities: ");
        pprint.pprint(activities)
        time.sleep(1)
        print("[+] Packages: " + str(packages))
        time.sleep(1)
        print("[+] Uses-Permissions: ");
        pprint.pprint(usesPermissions)
        time.sleep(1)
        print("[+] Permissions: ");
        pprint.pprint(permissions)
        time.sleep(1)
        print("[+] Receivers: ");
        pprint.pprint(receivers)
        time.sleep(1)
        print("[+] Receivers actions: ");
        pprint.pprint(recvsactions)
        time.sleep(1)
        input("Press enter when Virtual Android finish loading")
        # If we gonna use Logcat we need to clean the buffer
        adbHandler.cleanAdbLogcat()

        # If some error parsing AndroidManifest something strange happened, then exit
        if mainActivity == None:
            print("[-] No Main Activity where start...")
            sys.exit(-1)
        if packages == None:
            print("[-] No Packages...")
            sys.exit(-1)

        ret = subprocess.call(['monkeyrunner', 'monkeyFaren.py', apkFile, packages, mainActivity],
                              stderr=subprocess.PIPE, cwd=os.path.dirname(os.path.realpath(__file__)))

        if ret == 1:
            print("[-] Failed to start monkeyrunner")
            sys.exit(1)

        applicationStarted = 0
        stringApplicationStarted = "Start proc %s" % packages

        # Exec adb logcat with necessary  arguments
        adb = adbHandler.execAdbLogcat()

        logcatOutput = None
        # Now wait for Logcat output
        while True:
            try:
                logcatOutput = str(adb.stdout.readline())
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
            os.kill(adb.pid, signal.SIGKILL)
            sys.exit(-1)

        print("[+] Okey Application started, now start analysis")

        # create thread to count number of logs and start it
        logthread = adbClass.threadAnalyzer()
        logthread.start()

        timestamp = time.time()  # get current time
        # Finally start taking logs from logcat, we show the information as JSON
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
                            dexclass[time.time() - timestamp] = sentence['DexClassLoader']
                            logthread.increaseLogs()

                        # look for service started
                        if 'ServiceStart' in sentence:
                            # service started
                            sentence['ServiceStart']['type'] = 'service'
                            servicestart[time.time() - timestamp] = sentence['ServiceStart']
                            logthread.increaseLogs()

                        # received data from net
                        if 'RecvNet' in sentence:
                            host = sentence['RecvNet']['srchost']
                            port = sentence['RecvNet']['srcport']
                            recvdata = {'type': 'net read', 'host': host, 'port': port,
                                        'data': sentence['RecvNet']['data']}
                            recvnet[time.time() - timestamp] = recvdata
                            logthread.increaseLogs()

                        # fdaccess
                        if 'FdAccess' in sentence:
                            accessedfiles[sentence['FdAccess']['id']] = codecs.decode(sentence['FdAccess']['path'],
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

                            fdaccess[time.time() - timestamp] = sentence['FileRW']
                            logthread.increaseLogs()

                        # opened network connection log
                        if 'OpenNet' in sentence:
                            opennet[time.time() - timestamp] = sentence['OpenNet']
                            logthread.increaseLogs()

                        # closed socket
                        if 'CloseNet' in sentence:
                            closenet[time.time() - timestamp] = sentence['CloseNet']
                            logthread.increaseLogs()

                        # outgoing network activity log
                        if 'SendNet' in sentence:
                            sentence['SendNet']['type'] = 'net write'
                            sendnet[time.time() - timestamp] = sentence['SendNet']

                            logthread.increaseLogs()

                            # data leak log
                        if 'DataLeak' in sentence:
                            my_time = time.time() - timestamp
                            sentence['DataLeak']['type'] = 'leak'
                            sentence['DataLeak']['tag'] = adbClass.getTags(int(sentence['DataLeak']['tag'], 16))
                            dataleaks[my_time] = sentence['DataLeak']
                            logthread.increaseLogs()

                            if sentence['DataLeak']['sink'] == 'Network':
                                sentence['DataLeak']['type'] = 'net write'
                                sendnet[my_time] = sentence['DataLeak']
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
                                fdaccess[my_time] = sentence['DataLeak']
                                logthread.increaseLogs()

                            elif sentence['DataLeak']['sink'] == 'SMS':
                                sentence['DataLeak']['type'] = 'sms'
                                sendsms[my_time] = sentence['DataLeak']
                                logthread.increaseLogs()

                        # sent sms log
                        if 'SendSMS' in sentence:
                            sentence['SendSMS']['type'] = 'sms'
                            sendsms[time.time() - timestamp] = sentence['SendSMS']
                            logthread.increaseLogs()

                        # phone call log
                        if 'PhoneCall' in sentence:
                            sentence['PhoneCall']['type'] = 'call'
                            phonecalls[time.time() - timestamp] = sentence['PhoneCall']
                            logthread.increaseLogs()

                        # crypto api usage log
                        if 'CryptoUsage' in sentence:
                            sentence['CryptoUsage']['type'] = 'crypto'
                            cryptousage[time.time() - timestamp] = sentence['CryptoUsage']
                            logthread.increaseLogs()
                    except ValueError as e:
                        print("[-] ValueError: " + str(e))
                        errors.append(boxlog[1])
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
                # input()

        # KILL ADB LOGCAAAT
        os.kill(adb.pid, signal.SIGKILL)
        # Done? Store the objects in a dictionary, transform it in a JSON object and return it
        output = dict()

        # Sort the items by their key
        output["dexclass"] = dexclass
        output["servicestart"] = servicestart

        output["recvnet"] = recvnet
        output["opennet"] = opennet
        output["sendnet"] = sendnet
        output["closenet"] = closenet

        output["accessedfiles"] = accessedfiles
        output["dataleaks"] = dataleaks

        output["fdaccess"] = fdaccess
        output["sendsms"] = sendsms
        output["phonecalls"] = phonecalls
        output["cryptousage"] = cryptousage

        output["recvsaction"] = recvsactions
        output["enfperm"] = permissions

        output["hashes"] = hashes
        output["apkName"] = apkFile
        # sometimes there are errors in system image, but no problem 
        # we can show the logs with errors (usually crypto)
        output["errors"] = errors

        pp = pprint.PrettyPrinter(indent=4)

        pp.pprint(output)

        print(OKBLUE)
        print("############################################################")
        print(ENDC)

        sys.exit(0)
    ##################################### Do everything O.O
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

        ############################### Function by function
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
    os.system('clear')
    print(random.choice(bannerP))
    time.sleep(1)
    os.system('clear')
    print (banner)
    time.sleep(1)
    os.system('clear')
    print(OKBLUE)
    #print (secAdmin)
    #print (ciberSeg)
    print(ENDC)
    #time.sleep(2)
    os.system('clear')
    main()
