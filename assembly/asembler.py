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
    return ''

def assigStrCallback(i, c):
    global assigStrFlag
    assigStrFlag = True
    return h.STRCPY_FROM(control_stack.pop())

def jmpCallback(jump_type):
    global jmpFlag
    jmpFlag = True
    return jump_type

def putCallback(i, c):
    symbol = st.getByIndex(st.getIndexByName(control_stack.pop()))
    return h.PUT(symbol)

OPERATORS = {
    '+': lambda i, c : "\tFADD\n",
    '-': lambda i, c : "\tFSUB\n",
    '*': lambda i, c : "\tFMUL\n",
    '/': lambda i, c : "\tFDIV\n",
    ':=': assigCallback,
    'STRCPY': assigStrCallback,
    'CMP': lambda i, c : h.CMP(),
    'JLE': lambda i, c : jmpCallback("\tJBE "),
    'JL': lambda i, c : jmpCallback("\tJB "),
    'JGE': lambda i, c : jmpCallback("\tJNB "),
    'JG': lambda i, c : jmpCallback("\tJNBE "),
    'JE': lambda i, c : jmpCallback("\tJE "),
    'JNE': lambda i, c : jmpCallback("\tJNE "),
    'JZ': lambda i, c : jmpCallback("\tJNE "),
    'J': lambda i, c : jmpCallback("\tJMP "),
    'PUT': putCallback,
    'START_WHILE': lambda i, c : h.NEW_TAG(i+1),
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
            f.write(h.NEW_TAG(i))
            tagList.remove(i)
            
        if cell in OPERATORS:
            f.write(OPERATORS[cell](i, cell))
        elif assigFlag: 
            f.write(h.ASSIG(cell))
            assigFlag = False
        elif assigStrFlag: 
            f.write(h.STRCPY_TO(cell))
            assigStrFlag = False
        elif jmpFlag:
            cell_to_jump = cell.replace('[', '').replace(']', '')
            tagList.append(int(cell_to_jump))
            f.write(h.NEW_TAG(cell_to_jump))
            jmpFlag = False
        else:
            varType = st.getByIndex(st.getIndexByName(cell)).typeOf
            if varType != "STRING":
                f.write(h.FLD(cell))
            control_stack.append(cell)
            
            
    if len(tagList) != 0:
        for i in tagList:
            if i == len(polaca): f.write(h.NEW_TAG(i))
    f.write(h.CODE_END)


def run(polaca):
    print(st)
    with open('out/source.asm', 'w') as f:
        f.write(h.HEADER)
        writeVariables(f)
        writeCode(f, polaca)


# Todo
# . In - Validar Largo de String
# . Concat - Validar Largo de String
# . Not