from assembly import helpers as h
from lex import symbols_table

st = symbols_table.SymbolsTable()

assigFlag = False
def assigCallback():
    global assigFlag
    assigFlag = True
    return '\tFSTP '

OPERATORS = {
    '+': lambda : "\tFADD\n",
    '-': lambda : "\tFSUB\n",
    '*': lambda : "\tFMUL\n",
    '/': lambda : "\tFDIV\n",
    ':=': assigCallback,
}


def writeVariables(f):
    if st.getLastIndex() == -1: return
    
    f.write(h.VAR_START)
    for symbol in st.get():
        f.write(h.VAR(symbol))


def writeCode(f, polaca):
    global assigFlag
    f.write(h.CODE_START)
    
    for cell in polaca:
        if cell in OPERATORS:
            f.write(OPERATORS[cell]())
        elif assigFlag: 
            f.write(f'{cell}\n\tFFREE\n\n')
            assigFlag = False
        else:
            f.write(h.FLD(cell))
            
    f.write(h.CODE_END)


def run(polaca):
    with open('out/source.asm', 'w') as f:
        f.write(h.HEADER)
        writeVariables(f)
        writeCode(f, polaca)