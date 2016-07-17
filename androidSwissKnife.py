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
   _____              .___             .__    .___                 .__                 __          .__  _____       
  /  _  \   ____    __| _/______  ____ |__| __| _/   ________  _  _|__| ______ ______ |  | __ ____ |__|/ ____\____  
 /  /_\  \ /    \  / __ |\_  __ \/  _ \|  |/ __ |   /  ___/\ \/ \/ /  |/  ___//  ___/ |  |/ //    \|  \   __\/ __ \ 
/    |    \   |  \/ /_/ | |  | \(  <_> )  / /_/ |   \___ \  \     /|  |\___ \ \___ \  |    <|   |  \  ||  | \  ___/ 
\____|__  /___|  /\____ | |__|   \____/|__\____ |  /____  >  \/\_/ |__/____  >____  > |__|_ \___|  /__||__|  \___  >
        \/     \/      \/                      \/       \/                 \/     \/       \/    \/              \/ 
    ''',
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
called from app code.
If you added --exiftool flag with --apktool we will extract some meta-data
from some files with special extension.

Second use: --unzip

If you haven't got enough let's going to start with unzip function.
We will use unzip to extract data compressed in apk, because you know
an apk is like zip file.
Then we will show the certificate from the apk (not good quality but
you will have it in terminal)
Then list assets directory, maybe some cool things can be found here.
Now let's going to show some files can have interesting code.


Final Use: --all

Everything put together, live of color and music.
'''
######################################

def printDebug(string):

    global debug
    if debug:
        print (string)

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
    except Exception as e:
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
    print("%s"%ENDC)

    #close file
    amFile.close()
    #finally we return to directory 
    print('[+] Change directory to: '+actualDirectory)
    os.chdir(actualDirectory)

def readLibraries(directory):
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

    print('[+] Returning to directory: '+actualDirectory)
    os.chdir(actualDirectory)

###########################################################################

####################################UNZIP##################################
def unzipFunc(file):
    global outputName


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
    except Exception as e:
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
###########################################################################

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
            for root,dirs,files in os.walk('./assets'):
                for file in files:
                    if file.endswith('.jpg'):
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if pngFormat:
            for root,dirs,files in os.walk('./assets'):
                for file in files:
                    if file.endswith('.png'):
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if pdfFormat:
            for root,dirs,files in os.walk('./assets'):
                for file in files:
                    if file.endswith('.pdf'):
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if csvFormat:
            for root,dirs,files in os.walk('./assets'):
                for file in files:
                    if file.endswith('.csv'):
                        statement = 'exiftool '+os.path.join(root,file)
                        os.system(statement)
                        time.sleep(0.5)

        if txtFormat:
            for root,dirs,files in os.walk('./assets'):
                for file in files:
                    if file.endswith('.txt'):
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

def showTotalHelp():
    global totalHelp
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
    global allReal 
    

    help = '''
        ./androidSwissKnife.py [--man] -a <apk_file> -o <output_directories_name> [--apktool] [--unzip] [--exiftool] [--all]
        -a:     apk file in your directory or absolute path
        -o:     Name for output directories
        --apktool:  use apktool in Analysis
        --unzip: use unzip in Analysis
        --exiftool: use exiftool with some file formats
        --all: use all Analysis
        --man: get all the help from the program as star wars film

        Ejemplo:    ./androidSwissKnife.py -a dragonForce.apk -o analysis_dragon --apktool
    '''
    for index in range(len(sys.argv)):
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
        if sys.argv[index] == '--all':
            allReal = True

    if apkFile == '':
        print(help)
        sys.exit(0)
    if outputName == '':
        print(help)
        sys.exit(0)

    if (not apktoolUse) and (not unzipUse) and (not exiftoolUse) and (not allReal):
        print(help)
        sys.exit(0)

    if allReal:
        createApktoolFunc(apkFile)
        unzipFunc(apkFile)
    else:
        if apktoolUse:
            createApktoolFunc(apkFile)
        if unzipUse:
            unzipFunc(apkFile)
        

if __name__ == "__main__":
    print(random.choice(bannerP))
    time.sleep(3)
    print (banner)
    main()