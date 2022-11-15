from assembly import helpers as h
from lex import symbols_table

st = symbols_table.SymbolsTable()

assigFlag = False
jmpFlag = False
control_stack = []

def assigCallback():
    global assigFlag
    assigFlag = True
    return '\tFSTP '

def jmpCallback(jump_type):
    global jmpFlag
    jmpFlag = True
    return jump_type

OPERATORS = {
    '+': lambda : "\tFADD\n",
    '-': lambda : "\tFSUB\n",
    '*': lambda : "\tFMUL\n",
    '/': lambda : "\tFDIV\n",
    ':=': assigCallback,
    'CMP': lambda : "\tFXCH\n\tFCOM\n\tFSTSW AX\n\tSAHF\n",
    'JLE': lambda : jmpCallback("\tJBE"),
    'JL': lambda : jmpCallback("\tJB "),
    'JGE': lambda : jmpCallback("\tJNBE "),
    'JG': lambda : jmpCallback("\tJNB "),
    'JE': lambda : jmpCallback("\tJE "),
    'JNE': lambda : jmpCallback("\tJNE "),
    'JZ': lambda : jmpCallback("\tJNE "),
    'J': lambda : jmpCallback("\tJMP "),
    'PUT': lambda : f"\tMOV dx, OFFSET ESP | {control_stack.pop()}\n\tMOV ah,9\n\tint 21h\n",
    # 'GET':
}


def writeVariables(f):
    if st.getLastIndex() == -1: return
    
    f.write(h.VAR_START)
    for symbol in st.get():
        f.write(h.VAR(symbol))


def writeCode(f, polaca):
    global assigFlag, jmpFlag
    array_tmp = []
    f.write(h.CODE_START)
    
    for i, cell in enumerate(polaca):
        if i in array_tmp:
            f.write(f"_tag{i}: \n")

        if cell in OPERATORS:
            f.write(OPERATORS[cell]())
        elif assigFlag: 
            f.write(f'{cell}\n\tFFREE\n')
            assigFlag = False
        elif jmpFlag:
            cell_to_jump = cell.replace('[', '').replace(']', '')
            array_tmp.append(int(cell_to_jump))
            f.write(f"#tag{cell_to_jump}\n")
            jmpFlag = False
        else:
            if cell[0] != "@":
                f.write(h.FLD(cell))
            control_stack.append(cell)
            
    f.write(h.CODE_END)


def run(polaca):
    with open('out/source.asm', 'w') as f:
        f.write(h.HEADER)
        writeVariables(f)
        writeCode(f, polaca)


# Todo
# . If
# . While
# . In - Validar Largo de String
# . Out
# . Concat - Validar Largo de String
# . Not
# . Constante string no se debe cargar con FLD
# Se agrego al programa puntos de START y END START para que pueda compilarse el Assmebler