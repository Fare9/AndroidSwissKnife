#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
    Author: Fare9 <farenain9(at)gmail(dot)com>
    Program: AndroidSwissKnife
    Folder: Core
    File: Installer.py
'''

'''
    Installer of AndroidSwissKnife
'''

def install():
    '''
    Function to help the work of installing androidSwissKnife, maybe It's not perfect but you can take step by step manually
    
    :return: None
    :rtype: None
    '''
    toolsDir = "/opt/Tools"
    if os.geteuid() != 0:
        print("[-] You need to be root to install packages")
        exit(-1)

    os.mkdir(toolsDir)

    ASKDirectory = os.getcwd()

    print("[+] Creating symbolic links for androidSwissKnife")

    # link actual directory to variable path (directory where you have androidSwissKnife)
    os.system("echo PATH=\$PATH:" + ASKDirectory + " >> ~/.bashrc")

    # add permissions to exec
    os.system("chmod +x $PWD/AndroidSwissKnife.py")
    os.system("chmod +x $PWD/Libs/manifestDecoder.py")

    print("[+] Now you can call the tool anywhere with: AndroidSwissKnife.py")
    print("[+] Going to Directory Tools")
    os.chdir(toolsDir)

    print("[+] Installing last version of apktool")
    os.system("wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.2.3.jar")

    os.system("chmod +x ./apktool_2.2.3.jar")

    os.system("ln -sf $PWD/apktool_2.2.3.jar /usr/bin/apktool")

    print("[+] Installing last version of jadx")

    os.system("git clone https://github.com/skylot/jadx.git")
    os.chdir("jadx")

    os.system("./gradlew dist")
    os.system("ln -s $PWD/build/jadx/bin/jadx /usr/bin/jadx")
    os.system("ln -s $PWD/build/jadx/bin/jadx-gui /usr/bin/jadx-gui")
    
    os.chdir("..")  # Go to Tools
    print("[+] Installing gnome-terminal")
    os.system("sudo apt-get install gnome-terminal")


    print('[+] Installing pip3 ')
    os.system("sudo apt-get install python3-pip")


    print("[+] Installing exiftool")
    os.system('python3 %s/Libs/pyexiftool/setup.py install' % ASKDirectory)

    print("[+] Installing magic")
    os.system('python3 %s/Libs/python-magic/setup.py install' % ASKDirectory)

    print('[+] Installing libraries')
    os.system("pip3 install bytecode")
    os.system("pip3 install IPy")
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
    print("[+] Returning to: " + ASKDirectory)
