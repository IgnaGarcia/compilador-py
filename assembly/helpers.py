MAX_TEXT_SIZE = 120

HEADER = '''include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack
'''

VAR_START = f'''

.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ {MAX_TEXT_SIZE}
'''

CODE_START = '''

.CODE ; bloque de definicion de codigo

START:
mov AX,@DATA ; carga variables
mov DS,AX
mov es,ax

'''

CODE_END = ''' 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
'''

def VAR(symbol):
    if symbol.typeOf == "STRING":
        return f'''\t{symbol.name} \t\tDB \t\t"{symbol.value}", \'$\', {MAX_TEXT_SIZE-len(symbol.value)} dup (?) \n'''
    return f'''\t{symbol.name} \t\tDD \t\t{symbol.value} \n'''

def FLD(op):
    return f'''\tFLD {op}\n'''

def PUT(symbol):
    varType = symbol.typeOf
    displayType = ""
    if varType == "INT" or varType == "BOOL": 
        displayType = "DisplayInteger"
    elif varType == "REAL":
        displayType = "DisplayFloat"
    else: displayType = "displayString"
    return f"\t{displayType} {symbol.name}\nnewLine 1\n"

def NEW_TAG(idx):
    return f"\t_tag{idx}:\n"

def CMP():
    return "\tFXCH\n\tFCOM\n\tFSTSW AX\n\tSAHF\n"

def ASSIG(var):
    return f'\tFSTP {var}\n\tFREE\n'

def STRCPY_FROM(var):
    return f'\tMOV SI, OFFSET {var}\n'

def STRCPY_TO(var):
    return f'\tMOV DI, OFFSET {var}\n\tSTRCPY\n'