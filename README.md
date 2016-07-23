# AndroidSwissKnife
Program to make static analysis for Android APKs in python

'''python
/androidSwissKnife.py [--man] -a <apk_file> -o <output_directories_name> [--apktool] [--unzip] [--regEx <"regular Expression">] [--exiftool] [--all]
-a:     apk file in your directory or absolute path
-o:     Name for output directories
--apktool:  use apktool in Analysis
--unzip: use unzip in Analysis
--regEx: with unzip function we use a strings searching, you can add a regular Expression (by default URLs and Java Classes)
--exiftool: use exiftool with some file formats (you need first --apktool)
--all: use all Analysis
--man: get all the help from the program as star wars film

Ejemplo:    ./androidSwissKnife.py -a dragonForce.apk -o analysis_dragon --apktool
'''

'''python
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

'''python

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
'''

Follow the straw hat Pirates