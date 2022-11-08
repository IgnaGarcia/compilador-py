from assembly import helpers as h
from lex import symbols_table

st = symbols_table.SymbolsTable()

programStack = []

def writeVariables(f):
    if st.getLastIndex() == -1: return
    
    f.write(h.VAR_START)
    for symbol in st.get():
        f.write(h.variable(symbol))


def writeCode(f, polaca):
    f.write(h.CODE_START)
    f.write(h.CODE_END)


def run(polaca):
    with open('out/source.asm', 'w') as f:
        f.write(h.HEADER)
        writeVariables(f)
        writeCode(f, polaca)