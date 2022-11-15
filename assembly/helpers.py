MAX_TEXT_SIZE = 120

HEADER = '''include macros2.asm
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
    if symbol.typeOf == "BOOL":
        return f'''\t{symbol.name} \t\tDB \t\t{symbol.value} \n'''
    return f'''\t{symbol.name} \t\tDD \t\t{symbol.value} \n'''

def FLD(op):
    return f'''\tFLD {op}\n'''