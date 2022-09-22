from parser import yacc

tokens = ("PLUS", "MINUS")

def p_term(p):
    '''
    terminamos : factor
    '''
    p[0] = p[1]

def p_expression(p):
    '''
    expression : terminamos PLUS term
               | terminamos MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_error(e):
    print("UPS")

def parse(source):
    parser = yacc.yacc()    
    parser.parse(input=source, lexer=lexico)