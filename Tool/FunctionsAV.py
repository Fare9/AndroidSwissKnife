'''
    Modules to get functions from smali files,
    we will look for example calls or sms sends...

    I will use lex class for the lexical Analyzer
    ( as I learnt in "Procesadores del Lenguaje" in UAH)
'''


import ply.lex as lex

############################# TOKENS LEX #####################################

# tokens we want to find
tokens = (
            "CLASS",
            "METHOD",
            "INTENTS",
            "ACTIONCALL",
            "INIT_INTENT",
            "SET_DATA"
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

    print ("[+] Class: "+t.value+" in line: "+str(t.lineno))

# find methods
def t_METHOD(t):
    r"(\.method)[ ]+((public)|(private)|(protected))[ ]+[a-zA-Z].*\(.*\)[ZCBSIJFDV].*"

    print("\t[+] Method: "+t.value+" in line: "+str(t.lineno))


# Look for Intent object creation
def t_INTENTS(t):
    r"new-instance[ ]+v[0-9]+,[ ]*Landroid/content/Intent;"

    print("\t\t[+] New Intent: "+t.value+" in line: "+str(t.lineno))
# Look for action.CALL Strings
def t_ACTIONCALL(t):
    r"const-string[ ]+v[0-9]+,[ ]*(\"android.intent.action.CALL\")"

    print("\t\t[+] Action Call Strings: "+t.value+" in line: "+str(t.lineno))

# Catch Init Intent
# invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
# invoke-direct {v0, v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V
def t_INIT_INTENT(t):
    r"invoke-direct[ ]+{(p[0-9])?(v[0-9]?)(,[ ]*(p[0-9])?(v[0-9]?))*},[ ]*Landroid/content/Intent;-><init>[ ]*\(.*\)[ZCBSIJFDVL].*"

    print("\t\t[+] Init Intent: "+t.value+" in line: "+str(t.lineno))

# Catch SET DATA FOR INTENT
# invoke-virtual {v0, v1}, Landroid/content/Intent;->setData(Landroid/net/Uri;)Landroid/content/Intent;
def t_SET_DATA(t):
    r"invoke-virtual[ ]+{(p[0-9])?(v[0-9]?)(,[ ]*(p[0-9])?(v[0-9]?))*},[ ]*Landroid/content/Intent;->setData\(.*\)[ZCBSIJFDVL].*"

    print ("\t\t[+] Set Data: "+t.value+" in line: "+str(t.lineno))

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








