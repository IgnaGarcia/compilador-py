from lex import symbols_table as st

HEADER = '''
.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack
'''

def writeVariables(f):
    START = '''
.DATA ; bloque de definicion de variables
'''

def writeCode(f):
    START = '''
.CODE ; bloque de definicion de codigo
mov AX,@DATA : carga variables
mov DS,AX
mov es,ax ;'''
    END = ''' 
mov ax,4c00h
int 21h ; interrupcion del programca
END ; fin del programa
'''

def run(polaca):
    with open('out/source.asm', 'w') as f:
        f.write(HEADER)
        writeVariables(f)
        writeCode(f, polaca)