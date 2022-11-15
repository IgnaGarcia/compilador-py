from assembly import helpers as h
from lex import symbols_table

st = symbols_table.SymbolsTable()

assigFlag = False
assigStrFlag = False
jmpFlag = False
control_stack = []

def assigCallback(i, c):
    global assigFlag
    assigFlag = True
    return '\tFSTP '

def assigStrCallback(i, c):
    global assigStrFlag
    assigStrFlag = True
    return f'\tMOV SI, OFFSET {control_stack.pop()}\n'

def jmpCallback(jump_type):
    global jmpFlag
    jmpFlag = True
    return jump_type

def putCallback(i, c):
    symbol = st.getByIndex(st.getIndexByName(control_stack.pop()))
    varType = symbol.typeOf
    if varType == "INT" or varType == "BOOL":
        return f"\tDisplayInteger {symbol.name}\n"
    elif varType == "REAL":
        return f"\tDisplayFloat {symbol.name} 3\n"
    elif varType == "STRING":
        return f"\tdisplayString {symbol.name}\n"

OPERATORS = {
    '+': lambda i, c : "\tFADD\n",
    '-': lambda i, c : "\tFSUB\n",
    '*': lambda i, c : "\tFMUL\n",
    '/': lambda i, c : "\tFDIV\n",
    ':=': assigCallback,
    'STRCPY': assigStrCallback,
    'CMP': lambda i, c : "\tFXCH\n\tFCOM\n\tFSTSW AX\n\tSAHF\n",
    'JLE': lambda i, c : jmpCallback("\tJBE"),
    'JL': lambda i, c : jmpCallback("\tJB "),
    'JGE': lambda i, c : jmpCallback("\tJNB "),
    'JG': lambda i, c : jmpCallback("\tJNBE "),
    'JE': lambda i, c : jmpCallback("\tJE "),
    'JNE': lambda i, c : jmpCallback("\tJNE "),
    'JZ': lambda i, c : jmpCallback("\tJNE "),
    'J': lambda i, c : jmpCallback("\tJMP "),
    'PUT': putCallback,
    'START_WHILE': lambda i, c : f"_tag{i+1}:\n",
    # 'GET':
}


def writeVariables(f):
    if st.getLastIndex() == -1: return
    
    f.write(h.VAR_START)
    for symbol in st.get():
        f.write(h.VAR(symbol))


def writeCode(f, polaca):
    global assigFlag, assigStrFlag, jmpFlag
    tagList = []
    f.write(h.CODE_START)
    
    for i, cell in enumerate(polaca):
        if i in tagList:
            f.write(f"_tag{i}: \n")
            tagList.remove(i)
            
        if cell in OPERATORS:
            f.write(OPERATORS[cell](i, cell))
        elif assigFlag: 
            f.write(f'{cell}\n\tFFREE\n')
            assigFlag = False
        elif assigStrFlag: 
            f.write(f'\tMOV DI, OFFSET {cell}\n\tSTRCPY\n')
            assigStrFlag = False
        elif jmpFlag:
            cell_to_jump = cell.replace('[', '').replace(']', '')
            tagList.append(int(cell_to_jump))
            f.write(f"_tag{cell_to_jump}\n")
            jmpFlag = False
        else:
            varType = st.getByIndex(st.getIndexByName(cell)).typeOf
            if varType != "STRING":
                f.write(h.FLD(cell))
            control_stack.append(cell)
            
            
    if len(tagList) != 0:
        for tag in tagList:
            if tag == len(polaca): f.write(f'_tag{tag}:\n')
    f.write(h.CODE_END)


def run(polaca):
    print(st)
    with open('out/source.asm', 'w') as f:
        f.write(h.HEADER)
        writeVariables(f)
        writeCode(f, polaca)


# Todo
# . If
# . While
# . In - Validar Largo de String
# . Concat - Validar Largo de String
# . Not

# Revisar que no quede tag sin crear