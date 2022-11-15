from assembly import helpers as h
from lex import symbols_table

st = symbols_table.SymbolsTable()

assigFlag = False
assigStrFlag = False
jmpFlag = False
control_stack = []

def assigCallback():
    global assigFlag
    assigFlag = True
    return '\tFSTP '

def assigStrCallback():
    global assigStrFlag
    assigStrFlag = True
    return f'\tMOV SI, OFFSET {control_stack.pop()}\n'

def jmpCallback(jump_type):
    global jmpFlag
    jmpFlag = True
    return jump_type

def putCallback():
    symbol = st.getByIndex(st.getIndexByName(control_stack.pop()))
    varType = symbol.typeOf
    if varType == "INT" or varType == "BOOL":
        return f"\tDisplayInteger {symbol.name}\n"
    elif varType == "REAL":
        return f"\tDisplayFloat {symbol.name} 4\n"
    elif varType == "STRING":
        return f"\tdisplayString {symbol.name}\n"

OPERATORS = {
    '+': lambda : "\tFADD\n",
    '-': lambda : "\tFSUB\n",
    '*': lambda : "\tFMUL\n",
    '/': lambda : "\tFDIV\n",
    ':=': assigCallback,
    'STRCPY': assigStrCallback,
    'CMP': lambda : "\tFXCH\n\tFCOM\n\tFSTSW AX\n\tSAHF\n",
    'JLE': lambda : jmpCallback("\tJBE"),
    'JL': lambda : jmpCallback("\tJB "),
    'JGE': lambda : jmpCallback("\tJNBE "),
    'JG': lambda : jmpCallback("\tJNB "),
    'JE': lambda : jmpCallback("\tJE "),
    'JNE': lambda : jmpCallback("\tJNE "),
    'JZ': lambda : jmpCallback("\tJNE "),
    'J': lambda : jmpCallback("\tJMP "),
    'PUT': putCallback,
    # 'GET':
}


def writeVariables(f):
    if st.getLastIndex() == -1: return
    
    f.write(h.VAR_START)
    for symbol in st.get():
        f.write(h.VAR(symbol))


def writeCode(f, polaca):
    global assigFlag, assigStrFlag, jmpFlag
    array_tmp = []
    f.write(h.CODE_START)
    
    for i, cell in enumerate(polaca):
        if i in array_tmp:
            f.write(f"#tag{i}: \n")
            
        if cell in OPERATORS:
            f.write(OPERATORS[cell]())
        elif assigFlag: 
            f.write(f'{cell}\n\tFFREE\n')
            assigFlag = False
        elif assigStrFlag: 
            f.write(f'\tMOV DI, OFFSET {cell}\n\tSTRCPY\n')
            assigStrFlag = False
        elif jmpFlag:
            cell_to_jump = cell.replace('[', '').replace(']', '')
            array_tmp.append(int(cell_to_jump))
            f.write(f"#tag{cell_to_jump}\n")
            jmpFlag = False
        else:
            varType = st.getByIndex(st.getIndexByName(cell)).typeOf
            if varType != "STRING":
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

# sacar string de asignacion
