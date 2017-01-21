'''
	Variables for permissions, we will use this
	file for apktool module
'''

# Normal things¿?
normal_things = {}

normal_things['ACCESS_NETWORK_STATE'] = '\t[+] Mmm want to access ACCESS_NETWORK_STATE'
normal_things['ACCESS_WIFI_STATE'] = '\t[+] Mmm want to access ACCESS_WIFI_STATE'
normal_things['CHANGE_WIFI_STATE'] = '\t[+] Mmm want to access CHANGE_WIFI_STATE'


# Some things to worry about
strange_things = {}

strange_things['CAMERA'] = '\t[+] Mmm want to access CAMERA, look for NSA spy'
strange_things['hardware.camera'] = '\t[+] Mmm just for devices with CAMERAAAA'
strange_things['READ_CONTACTS'] = '\t[+] Mmm want to READ_CONTACTS, take a look'
strange_things['RECORD_AUDIO'] = '\t[+] Mmm want to RECORD_AUDIO, I hope you must press a button for that'
strange_things['WRITE_SETTINGS'] = '\t[+] Ohh Want to WRITE_SETTINGS,bad...bad...bad'
strange_things['RECEIVE_BOOT_COMPLETED'] = '\t[+] This process wants to run at boot completed'
strange_things['ACTION_BOOT_COMPLETED'] = '\t[+] This process wants to run at boot completed'
strange_things['READ_PHONE_STATE'] = '\t[+] READ_PHONE_STATE, wanna check phone constants?'
# PROBLEM THINGS
problem_things = {}

problem_things['SEND_SMS'] = '\t[+] Ohh want to SEND_SMS'
problem_things['RECEIVE_SMS'] = '\t[+] Ohh want to RECEIVE_SMS look for receiver in code'
problem_things['READ_SMS'] = '\t[+] Ohh want to READ_SMS look for receiver in code'
problem_things['WRITE_SMS'] = '\t[+] Ohh want to WRITE_SMS'
problem_things['WRITE_CONTACTS'] = '\t[+] Why want to WRITE_CONTACTS ?'
problem_things['CALL_PHONE'] = '\t[+] Oh really? accept CALL_PHONE'
problem_things['PROCESS_OUTGOING_CALLS'] = '\t[+] Mother of Edward Snowden, PROCESS_OUTGOING_CALLS O.O'
problem_things['KILL_BACKGROUND_PROCESSES'] = '\t[+] KILL_BACKGROUND_PROCESSES, even Demi Lovato wouldn\'t accept this app '
problem_things['MOUNT_UNMOUNT_FILESYSTEMS'] = '\t[+] Wants to MOUNT_UMOUNT_FILESYSTEMS... That\'s not good'

