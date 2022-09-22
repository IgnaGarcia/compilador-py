from parser import yacc

tokens = ("ID", "CTE_NUMERICA", "CTE_REAL", "CTE_STRING",
          "LLAVE_ABRE", "LLAVE_CIERRA", "PARENTESIS_ABRE", "PARENTESIS_CIERRA",
          "PUNTO_COMA","COMA",
          "OP_RESTA", "OP_SUMA", "OP_DIVISION", "OP_MULTIPLICACION", "OP_CONCAT",
          "COMP_MENOR", "COMP_MAYOR", "COMP_MENOR_IGUAL", "COMP_MAYOR_IGUAL", 
          "COMP_IGUAL", "COMP_DISTINTO",
          "OP_OR", "OP_AND", "OP_NOT",
          "OP_ASIGNACION", "CONDICION_TERNARIA", "DOS_PUNTOS",
          "while", "if", "else", "between", "out", "in", 
          "var", "string", "int", "real", "bool", "true", "false")
    

def p_factor(p):
    '''
    factor : CTE_NUMERICA
        | CTE_REAL
        | ID
    '''    
    p[0] = p[1]


def p_term(p):
    '''
    term : term OP_MULTIPLICACION factor
        | term OP_DIVISION factor 
        | factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    p[0] = p[1]


def p_expression(p):
    '''
    expression : expression OP_SUMA term
                | expression OP_RESTA term
                | term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    p[0] = p[1]

def p_statements(p):
    '''
    statements : statement
                | statements statement
    '''
    p[0] = p[1] if len(p) == 2 else p[1] + p[2]

def p_statement(p):
    '''
    statement : asignacion
	            | if
	            | while
	            | between
    '''
    p[0] = p[1]

def p_error(e):
    print("UPS")


def parse(source):
    parser = yacc.yacc()    
    parser.parse(input=source, lexer=lexico)