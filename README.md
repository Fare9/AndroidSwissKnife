# AndroidSwissKnife
FrameWork to make static and dynamic analysis for Android APKs in Python
If you want to ask me for changes you want to add (for example in AndroidManifest analysis), 
write to my email address: farenain9@gmail.com

```python
    help = '''
        ./androidSwissKnife.py [--install] [--man] -a <apk_file> -o <output_directories_name> [--apktool] [--unzip] [--regEx <"regular Expression">] [--exiftool] [--jadx] [--opcodes] [--all] [--create-apk -f <folder from apktool> -apk <name for apk>] [--connect <IP:port>] [--DroidBox]
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
        --connect: Connect to android device with adb
        --all: use all Analysis
        --create-apk: generate an apk, from apktool folder
        --man: get all the help from the program as star wars film
        --DroidBox: New feature to do a dynamic analysis of the apk (It's a "wrapper" of droidbox with Burpsuite)

        Ejemplo:    ./androidSwissKnife.py -a dragonForce.apk -o analysis_dragon --apktool
    '''
```

```python
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

###### NEW FEATURES ########
--create-apk
Once you have used apktool to get smali code from an apk, you can modify it, and finally
create another apk with your changes, you can use this feature to do it.

### FINALLY DYNAMIC ANALYSIS (DroidBox Wrapper)
--DroidBox
I modified DroidBox code to this framework, I rewrite some functions to work in python3
but nothing change from this program. You need to have an android emulator, in Readme.md
you can see the features of my emulator.
'''


```

Features for android Emulator
<p></p>
<img src="./anemf.png" />
<img src="./ASKN.png" width="672"/>
<img src="./StrawHat.png" width="516"/>


Follow the straw hat Pirates