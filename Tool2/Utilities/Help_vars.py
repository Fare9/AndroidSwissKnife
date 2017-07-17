#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Utilities
    File: Help_vars
'''

'''
	Any help information to add will be here
'''

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
