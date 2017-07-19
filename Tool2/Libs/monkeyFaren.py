#/usr/bin/env python3

"""
    My version of the file monkeyrunner
    from DroidBox Dynamic Analyzer 

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
"""


import sys

# This library will give us every function we need for Android
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

import subprocess
import logging
import time

# This program has been called from androidSwissKnife , we pass some arguments
apkName = sys.argv[1]
package = sys.argv[2]
Mainactivity = sys.argv[3]

# before call this program we started an emulator
androidDevice = None

# we will wait for the emulator and then install apk
i = 1
for r in range(9):
    dots = '.' * i
    sys.stdout.write("                                            \r")
    sys.stdout.write("Waiting for emulator"+str(dots)+"\r")
    sys.stdout.flush()  
    time.sleep(0.5)
    i = i + 1
    if i == 4:
        i = 1
while androidDevice == None:
    try:
        print("Waiting for emulator...")
        # now we wait for emulator 3 seconds of timeout
        androidDevice = MonkeyRunner.waitForConnection(3)
    except:
        pass

# since this moment, we will use functions from monkeyrunner
print("[+] Installing the application %s..." % apkName)
androidDevice.installPackage(apkName)

# Now create the name for MainActivity to start for example:
#
#   package: .cnt   MainActivity: Class     Path = .cnt./.cnt.Class
#   package: com.cnt    MainActivity: Class Path = com.cnt/Class
#   package: cnt    MainActivity: Class     Path = cnt/cnt.Class

if "." in Mainactivity:
    if Mainactivity.startswith('.'):
        runComponent = "%s/%s%s" % (package, package, Mainactivity)
    else:
         runComponent = "%s/%s" % (package, Mainactivity)
else:
    runComponent = "%s/%s.%s" % (package, package, Mainactivity)


print("[+] Running the component %s..." % (runComponent))

# Now start MainActivity, we execute it in child process with Popen, with STDOUT send to a PIPE
p = subprocess.Popen(["adb", "shell", "am", "start", "-n", runComponent], stdout=subprocess.PIPE)
# we use the pipe to get output
output, error = p.communicate()

#Activity not started?
if "Error type" in output:
    print("[-] ERROR starting Main")
    sys.exit(1)
else:
    print("[+] Succesfully exit MonkeyFaren")
    sys.exit(0)