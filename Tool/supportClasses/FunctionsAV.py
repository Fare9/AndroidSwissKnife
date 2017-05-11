'''
    Modules to get functions from smali files,
    we will look for example calls or sms sends...

    I will use lex class for the lexical Analyzer
    ( as I learnt in "Procesadores del Lenguaje" in UAH)

    If you have to resolve a problem with regular expression,
    well, you have two problems
'''

HEADER  = '\033[95m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'


import ply.lex as lex

############################# TOKENS LEX #####################################

# tokens we want to find
tokens = (
            "CLASS",
            "METHOD",
            "INTENTS",
            # For Calls methods
            "ACTIONCALL",
            "INIT_INTENT",
            "SET_DATA",
            "START_ACTIVITY",
            # FOR SMS API MANAGER
            "SMSMANAGER_GETDEFAULT",
            "SMSMANAGER_SENDTEXTMESSAGE",
            # FOR HARDCODED EMAILS
            "EMAILS"

        )


############################# TOKENS DEFINITION ###############################

# regular expressions for tokens

# things to ignore
t_ignore = "\t\r"



# A method definition setting the regular expression for a class
# and running an action

# find classes
def t_CLASS(t):
    r"(\.class)[ ]+((public)|(private)|(protected))[ ]+L[^;]+?;"
    print (OKBLUE+"[+] Class: "+t.value+" in line: "+str(t.lineno)+ENDC)

# find methods
def t_METHOD(t):
    r"(\.method)[ ]+((public)|(private)|(protected))[ ]+[a-zA-Z].*\(.*\)[ZCBSIJFDV].*"
    print(OKGREEN+"\t[+] Method: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Look for Intent object creation
def t_INTENTS(t):
    r"new-instance[ ]+v[0-9]+,[ ]*Landroid/content/Intent;"
    print(WARNING+"\t\t[+] New Intent: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Look for action.CALL Strings
def t_ACTIONCALL(t):
    r"const-string[ ]+v[0-9]+,[ ]*(\"android.intent.action.CALL\")"
    print(FAIL+"\t\t[+] Action Call Strings: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Catch Init Intent
# invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
# invoke-direct {v0, v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V
def t_INIT_INTENT(t):
    r"invoke-direct[ ]+{(p[0-9])?(v[0-9]?)(,[ ]*(p[0-9])?(v[0-9]?))*},[ ]*Landroid/content/Intent;-><init>[ ]*\(.*\)[ZCBSIJFDVL].*"
    print(WARNING+"\t\t[+] Init Intent: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Catch SET DATA FOR INTENT
# invoke-virtual {v0, v1}, Landroid/content/Intent;->setData(Landroid/net/Uri;)Landroid/content/Intent;
def t_SET_DATA(t):
    r"invoke-virtual[ ]+{(p[0-9])?(v[0-9]?)(,[ ]*(p[0-9])?(v[0-9]?))*},[ ]*Landroid/content/Intent;->setData\(.*\)[ZCBSIJFDVL].*"
    print (FAIL+"\t\t[+] Set Data: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Catch START ACTIVITY
# invoke-virtual {p0, v0}, Lcom/example/root/proofsmalware/MainActivity;->startActivity(Landroid/content/Intent;)V
# invoke-virtual {p1, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V
def t_START_ACTIVITY(t):
    r"invoke-virtual[ ]*{(p[0-9])?(v[0-9])?(,[ ]*(p[0-9])?(v[0-9])?)?},[ ]*L[^;]+?;->startActivity\(.*\)[ZCBSIJFDVL].*"

    print(WARNING+"\t\t[+] Start Activity: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Catch GetDefaults from sms api
# invoke-static {}, Landroid/telephony/SmsManager;->getDefault()Landroid/telephony/SmsManager;
def t_SMSMANAGER_GETDEFAULT(t):
    r"invoke-static[ ]*{(p[0-9])?(v[0-9])?(,[ ]*(p[0-9])?(v[0-9])?)?},[ ]*Landroid/telephony/SmsManager;->getDefault\(.*\)[ZCBSIJFDVL].*"
    print(FAIL+"\t\t[+] Get Default SMS API: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Catch SendSMS
# invoke-virtual/range {v0 .. v5}, Landroid/telephony/SmsManager;->sendTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)V
def t_SMSMANAGER_SENDTEXTMESSAGE(t):
    r"invoke-virtual/range[ ]*{(p[0-9])?(v[0-9])?[ ]*\.\.[ ]*(p[0-9])?(v[0-9])?},[ ]*Landroid/telephony/SmsManager;->sendTextMessage\(.*\)[ZCBSIJFDVL].*"

    print(FAIL+"\t\t[+] Send Text Message API: "+t.value+" in line: "+str(t.lineno)+ENDC)

# Catch Emails
# example@example.com
def t_EMAILS(t):
    r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(FAIL+"\t\t[+] Email in code: "+t.value+" in line: "+str(t.lineno)+ENDC)
# method to catch errors
def t_error(t):

    #print ("[-] Error: "+t.value[0])
    t.lexer.skip(1)

# Set new line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# End of file
def t_eof(t):
    print ("[!] Finished program")

filed = open("/root/Documentos/ProgramasSMALI/apktool-proofsmalware/smali/com/example/root/proofsmalware/MainActivity.smali","rb")

# Build lexical analyzer
lex.lex()
lex.input(filed.read())

filed.close()
# Obtener los tokens.
while 1:
    tok = lex.token()
    if not tok:
        break
    print (tok)








