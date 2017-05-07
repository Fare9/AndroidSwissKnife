'''
    Some useful methods, I will explain every method
    and where i call it
'''

def parseObjDump(text,file_):
    '''
        I will parse output of objdump, something like this:
        0000dd75 g    DF .text  00000026 Java_com_Titanium_Magister_sursumApp_nativesursumAppCall

        We will call this method from readLibraries in androidSwissKnife.py
    '''
    output = []
    lines = text.split(b'\n')
    for line in lines:
        if len(line) < 1:
            continue
        dictionary = {}
        line = str(line)
        line = line.strip()
        line = line.replace('\\t',' ')

        strippedLine = line.split()

        dictionary['symbol_value'] = strippedLine[0]
        dictionary['symbols'] = strippedLine[1]
        if dictionary['symbols'] == 'l':
            dictionary['kind_symbol'] = 'local'

        elif dictionary['symbols'] == 'g':
            dictionary['kind_symbol'] = 'global'

        elif dictionary['symbols'] == 'u':
            dictionary['kind_symbol'] = 'unique global'

        elif dictionary['symbols'] == '!':
            dictionary['kind_symbol'] = 'both or neither (global/local)'

        elif dictionary['symbols'] == 'w':
            dictionary['kind_symbol'] = 'weak or strong symbol'

        elif dictionary['symbols'] == 'C':
            dictionary['kind_symbol'] = 'Constructor'

        elif dictionary['symbols'] == 'W':
            dictionary['kind_symbol'] = 'Warning'

        elif dictionary['symbols'] == 'd':
            dictionary['kind_symbol'] = 'Debugging symbol'

        elif dictionary['symbols'] == 'D':
            dictionary['kind_symbol'] = 'Dynamic symbol'

        elif dictionary['symbols'] == 'F':
            dictionary['kind_symbol'] = 'Symbol is a Function name'

        elif dictionary['symbols'] == 'f':
            dictionary['kind_symbol'] = 'Symbol is a File name'
        
        elif dictionary['symbols'] == 'O':
            dictionary['kind_symbol'] = 'Symbol is a Object name'

        #print(dictionary['kind_symbol'])
        dictionary['section'] = strippedLine[3]
        #print(dictionary['section'])
        dictionary['size'] = strippedLine[4]
        #print(dictionary['size'])
        dictionary['method'] = strippedLine[5]
        #print(dictionary['method'])

        output.append(dictionary)

    return {"File":file_,"Methods":output}


