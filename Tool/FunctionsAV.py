'''
    Modules to get functions from smali files,
    we will look for example calls or sms sends...
'''

# for regular expression
import ply.lex as lex


# tokens we want to find
tokens = (
            "CLASS",
            "METHOD",
            "STRING",
            "INTENTS"
        )

# regular expressions for tokens
t_ignore = "\t\r"

# .class public Lcom/example/root/proofsmalware/MainActivity;
#


# A method definition setting the regular expression for a class
# and running an action
def t_CLASS(t):
    r"(\.class)[ ]+((public)|(private)|(protected))[ ]+L[^;]+?;"

    print ("[+] Class: "+t.value)

# method to catch errors
def t_error(t):

    #print ("[-] Error: "+t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

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








