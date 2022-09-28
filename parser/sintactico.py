from parser import yacc
from lex import lexico


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


# ------------------------- Rules
## ------------------------------ Program 
def p_program(p):
    ''' program : variables_block statements '''
    # p[0] = p[1]
    pass

def p_program(p):
    ''' program : statements '''
    # p[0] = p[1]
    pass

def p_program(p):
    ''' program : statements '''
    # p[0] = p[1]
    pass


## ------------------------------ Declaration of Variables
def p_variables_block(p):
    ''' variables_block : var LLAVE_ABRE variables_list LLAVE_CIERRA '''
    pass

def p_variables_list(p):
    ''' variables_list : variables_list variable_declaration '''
    pass

def p_variables_list(p):
    ''' variables_list : variable_declaration '''
    pass

def p_variable_declaration(p):
    ''' variable_declaration : variable_type variables_names PUNTO_COMA '''
    pass

def p_variables_names(p):
    ''' variables_names : variables_name COMA ID '''
    pass

def p_variables_names(p):
    ''' variables_names : ID '''
    pass

### ----------------------------------- Variable Types
def p_variable_type(p):
    ''' variable_type : int '''
    pass

def p_variable_type(p):
    ''' variable_type : real '''
    pass

def p_variable_type(p):
    ''' variable_type : string '''
    pass

def p_variable_type(p):
    ''' variable_type : bool '''
    pass


## ------------------------------ Statements
def p_statements(p):
    ''' statements : statement '''
    # p[0] = p[1]
    pass
    
def p_statements(p):
    ''' statements : statements statement '''
    # p[0] = p[1] + p[2]
    pass

def p_statement(p):
    ''' statement : assignment_statement '''
    # p[0] = p[1]
    pass

def p_statement(p):
    ''' statement : if_statement '''
    # p[0] = p[1]
    pass

def p_statement(p):
    ''' statement : while_statement '''
    # p[0] = p[1]
    pass

def p_statement(p):
    ''' statement : in_statement '''
    # p[0] = p[1]
    pass

def p_statement(p):
    ''' statement : out_statement '''
    # p[0] = p[1]
    pass

### ----------------------------------- Out Statement
def p_out_statement(p):
    ''' out_statement : str_expression PUNTO_COMA '''
    # p[0] = p[1]
    pass

### ----------------------------------- In Statement
def p_in_statement(p):
    ''' in_statement : ID PUNTO_COMA '''
    # p[0] = p[1]
    pass


## ------------------------------ Arithmetic Operations
### ----------------------------------- Expression
def p_expression(p):
    ''' expression : expression OP_SUMA term '''
    # p[0] = p[1] + p[3]
    pass
    
def p_expression(p):
    ''' expression : expression OP_RESTA term '''
    # p[0] = p[1] - p[3]
    pass

def p_expression(p):
    ''' expression : term '''
    # p[0] = p[1]
    pass

### ----------------------------------- Term
def p_term(p):
    ''' term : term OP_MULTIPLICACION factor '''
    # p[0] = p[1] * p[3]
    pass
    
def p_term(p):
    ''' term : term OP_DIVISION factor '''
    # p[0] = p[1] / p[3]
    pass
    
def p_term(p):
    ''' term : factor '''
    # p[0] = p[1]
    pass
    
### ----------------------------------- Factor
def p_factor(p):
    ''' factor : CTE_NUMERICA ''' 
    # p[0] = p[1]
    pass
    
def p_factor(p):
    ''' factor : CTE_REAL ''' 
    # p[0] = p[1]
    pass
    
def p_factor(p):
    ''' factor : ID ''' 
    # p[0] = p[1]
    pass


## ------------------------------ String Expression
def p_str_expression(p):
    ''' str_expression : str_term OP_SUMA OP_SUMA str_term '''
    pass

def p_str_expression(p):
    ''' str_expression : str_term '''
    pass

def p_str_term(p):
    ''' str_term : CTE_STRING '''
    # p[0] = p[1]
    pass
    
def p_str_term(p):
    ''' str_term : ID '''
    # p[0] = p[1]
    pass


## ------------------------------ Comparision Operations
def p_comparision(p):
    ''' comparision : expresion op_comparision expresion '''
    pass

def p_comparision(p):
    ''' comparision : str_expression op_comparision str_expression '''
    pass

### ----------------------------------- Comparision Operators
def p_op_comparision(p):
    ''' op_comparision : COMP_MENOR '''
    pass

def p_op_comparision(p):
    ''' op_comparision : COMP_MAYOR '''
    pass

def p_op_comparision(p):
    ''' op_comparision : COMP_MENOR_IGUAL '''
    pass

def p_op_comparision(p):
    ''' op_comparision : COMP_MAYOR_IGUAL '''
    pass

def p_op_comparision(p):
    ''' op_comparision : COMP_IGUAL '''
    pass

def p_op_comparision(p):
    ''' op_comparision : COMP_DISTINTO '''
    pass


## ------------------------------ Logical Expressions
### ----------------------------------- Logical Statement
def p_logical_statement(p):
    ''' logical_statement : logical_expression '''
    pass

def p_logical_statement(p):
    ''' logical_statement : logical_expression op_logic logical_expression '''
    pass

### ----------------------------------- Logical Expression
def p_logical_expression(p):
    ''' logical_expression : OP_NOT logical_term '''
    pass

def p_logical_expression(p):
    ''' logical_expression : logical_term '''
    pass

### ----------------------------------- Logical Term
def p_logical_term(p):
    ''' logical_term : comparision '''
    pass

def p_logical_term(p):
    ''' logical_term : between_statement '''
    pass

def p_logical_term(p):
    ''' logical_term : cte_logic '''
    pass

### ----------------------------------- Logical Operators
def p_op_logic(p):
    ''' op_logic : OP_OR '''
    pass

def p_op_logic(p):
    ''' op_logic : OP_AND '''
    pass

### ----------------------------------- Logical Constants
def p_cte_logic(p):
    ''' cte_logic : true '''
    pass

def p_cte_logic(p):
    ''' cte_logic : false '''
    pass

### ----------------------------------- Between Statement
def p_between_statement(p):
    ''' between_statement : between PARENTESIS_ABRE ID COMA expression DOS_PUNTOS expression PARENTESIS_CIERRA '''
    pass


## ------------------------------ Assignment Statement
def p_assignment_statementt(p):
    ''' assignment_statement : ID OP_ASIGNACION assignment_value PUNTO_COMA '''
    pass

def p_assignment_value(p):
    ''' assignment_value : ternary '''
    pass

def p_assignment_value(p):
    ''' assignment_value : expression '''
    pass

def p_assignment_value(p):
    ''' assignment_value : str_expression '''
    pass

def p_assignment_value(p):
    ''' assignment_value : logical_statement '''
    pass

### ----------------------------------- Ternary Operator
def p_ternary(p):
    ''' ternary : condicion CONDICION_TERNARIA expression DOS_PUNTOS expression '''
    pass

def p_ternary(p):
    ''' ternary : condicion CONDICION_TERNARIA str_expression DOS_PUNTOS str_expression '''
    pass


## ------------------------------ Error Rule
def p_error(e):
    print(e)


def parse(source):
    parser = yacc.yacc()  
    parser.parse(input=source, lexer=lexico.Lexer())