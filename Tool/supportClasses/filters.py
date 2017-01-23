'''
    Variable for filters that can cause some problems
'''

filterString = {}


# android.provider.Telephony
filterString['android.provider.Telephony.SMS_RECEIVED'] = "\t[+] Want to get if you have a new SMS_RECEIVED"
filterString['android.provider.Telephony.SMS_DELIVER'] = "\t[+] Have you SMS_DELIVER? The app knows the app knows it too"
filterString['android.provider.Telephony.SIM_FULL'] = "\t[+] Trump and this app know that your SIM_FULL"


# android.intent.action
filterString['android.intent.action.ANSWER'] = "\t[+] This APP can handle your incoming calls with ANSWER"
filterString['android.intent.action.ALL_APPS'] = "\t[+] Can list ALL_APPS, for example AV engines =)"
filterString['android.intent.action.BOOT_COMPLETED'] = "\t[+] When BOOT_COMPLETED this app can start"
