from assembly import helpers as h
from lex import symbols_table

st = symbols_table.SymbolsTable()

assigFlag = False
jmpFlag = False

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
    'JLE': lambda : jmpCallback("\tJB "),
    'JL': lambda : jmpCallback("\tJB "),
    'JGE': lambda : jmpCallback("\tJNBE "),
    'JG': lambda : jmpCallback("\tJNB "),
    'JE': lambda : jmpCallback("\tJE "),
    'JNE': lambda : jmpCallback("\tJNE "),
    'JZ': lambda : jmpCallback("\tJNE "),
    'J': lambda : jmpCallback("\tJMP "),
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
        print(array_tmp)
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
            f.write(f"_tag{cell_to_jump}\n")
            jmpFlag = False
        else:
            f.write(h.FLD(cell))
            
    f.write(h.CODE_END)


def run(polaca):
    with open('out/source.asm', 'w') as f:
        f.write(h.HEADER)
        writeVariables(f)
        writeCode(f, polaca)