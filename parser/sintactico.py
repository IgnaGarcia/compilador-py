from parser import yacc
from lex import lexico

log = True

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
def p_program_with_variables(p):
    ''' program : variables_block statements '''
    if log:
        print(''' program : variables_block statements ''')
    # p[0] = p[1]
    pass

def p_program(p):
    ''' program : statements '''
    if log:
        print(''' program : statements ''')
    # p[0] = p[1]
    pass


## ------------------------------ Declaration of Variables
def p_variables_block(p):
    ''' variables_block : var LLAVE_ABRE variables_list LLAVE_CIERRA '''
    if log:
        print(''' variables_block : var LLAVE_ABRE variables_list LLAVE_CIERRA ''')
    pass

def p_variables_list_r(p):
    ''' variables_list : variables_list variable_declaration '''
    if log:
        print(''' variables_list : variables_list variable_declaration ''')
    pass

def p_variables_list(p):
    ''' variables_list : variable_declaration '''
    if log:
        print(''' variables_list : variable_declaration ''')
    pass

def p_variable_declaration(p):
    ''' variable_declaration : variable_type variables_names PUNTO_COMA '''
    if log:
        print(''' variable_declaration : variable_type variables_names PUNTO_COMA ''')
    pass

def p_variables_names_r(p):
    ''' variables_names : variables_names COMA ID '''
    if log:
        print(''' variables_names : variables_names COMA ID ''')
    pass

def p_variables_names(p):
    ''' variables_names : ID '''
    if log:
        print(''' variables_names : ID ''')
    pass

### ----------------------------------- Variable Types
def p_variable_type_int(p):
    ''' variable_type : int '''
    if log:
        print(''' variable_type : int ''')
    pass

def p_variable_type_real(p):
    ''' variable_type : real '''
    if log:
        print(''' variable_type : real ''')
    pass

def p_variable_type_string(p):
    ''' variable_type : string '''
    if log:
        print(''' variable_type : string ''')
    pass

def p_variable_type_bool(p):
    ''' variable_type : bool '''
    if log:
        print(''' variable_type : bool ''')
    pass


## ------------------------------ Statements
def p_statements(p):
    ''' statements : statement '''
    if log:
        print(''' statements : statement ''')
    # p[0] = p[1]
    pass
    
def p_statements_r(p):
    ''' statements : statements statement '''
    if log:
        print(''' statements : statements statement ''')
    # p[0] = p[1] + p[2]
    pass

def p_statement_assignment(p):
    ''' statement : assignment_statement '''
    if log:
        print(''' statement : assignment_statement ''')
    # p[0] = p[1]
    pass

def p_statement_select(p):
    ''' statement : select_statement '''
    if log:
        print(''' statement : select_statement ''')
    # p[0] = p[1]
    pass

def p_statement_while(p):
    ''' statement : while_statement '''
    if log:
        print(''' statement : while_statement ''')
    # p[0] = p[1]
    pass

def p_statement_in(p):
    ''' statement : in_statement '''
    if log:
        print(''' statement : in_statement ''')
    # p[0] = p[1]
    pass

def p_statement_out(p):
    ''' statement : out_statement '''
    if log:
        print(''' statement : out_statement ''')
    # p[0] = p[1]
    pass

### ----------------------------------- While Statement
def p_while_statement(p):
    ''' while_statement : while logical_statement LLAVE_ABRE statements LLAVE_CIERRA '''
    if log:
        print(''' while_statement : while logical_statement LLAVE_ABRE statements LLAVE_CIERRA ''')
    pass

### ----------------------------------- Select Statement
def p_select_statement_with_else(p):
    ''' select_statement : if_statement else_if_statement '''
    if log:
        print(''' select_statement : if_statement else_if_statement ''')
    pass

def p_select_statement(p):
    ''' select_statement : if_statement '''
    if log:
        print(''' select_statement : if_statement ''')
    pass

def p_if_statement(p):
    ''' if_statement :  if logical_statement LLAVE_ABRE statements LLAVE_CIERRA '''
    if log:
        print(''' if_statement :  if logical_statement LLAVE_ABRE statements LLAVE_CIERRA ''')
    pass

def p_else_if_statement(p):
    ''' else_if_statement : else if_statement '''
    if log:
        print(''' else_if_statement : else if_statement ''')
    pass

def p_else_if_statement_r(p):
    ''' else_if_statement : else_if_statement else if_statement '''
    if log:
        print(''' else_if_statement : else_if_statement else if_statement ''')
    pass

def p_else_if_statement_r_with_else(p):
    ''' else_if_statement : else_if_statement else_statement '''
    if log:
        print(''' else_if_statement : else_if_statement else_statement ''')
    pass

def p_else_statement(p):
    ''' else_statement : else LLAVE_ABRE statements LLAVE_CIERRA '''
    if log:
        print(''' else_statement : else LLAVE_ABRE statements LLAVE_CIERRA ''')
    pass

### ----------------------------------- Out Statement
def p_out_statement(p):
    ''' out_statement : out str_expression PUNTO_COMA '''
    if log:
        print(''' out_statement : out str_expression PUNTO_COMA ''')
    # p[0] = p[1]
    pass

### ----------------------------------- In Statement
def p_in_statement(p):
    ''' in_statement : in ID PUNTO_COMA '''
    if log:
        print(''' in_statement : in ID PUNTO_COMA ''')
    # p[0] = p[1]
    pass


## ------------------------------ Arithmetic Operations
### ----------------------------------- Expression
def p_expression_plus(p):
    ''' expression : expression OP_SUMA term '''
    if log:
        print(''' expression : expression OP_SUMA term ''')
    # p[0] = p[1] + p[3]
    pass
    
def p_expression_minus(p):
    ''' expression : expression OP_RESTA term '''
    if log:
        print(''' expression : expression OP_RESTA term ''')
    # p[0] = p[1] - p[3]
    pass
    
def p_expression_negative(p):
    ''' expression : OP_RESTA term '''
    if log:
        print(''' expression : OP_RESTA term ''')
    # p[0] = p[1] - p[3]
    pass

def p_expression(p):
    ''' expression : term '''
    if log:
        print(''' expression : term ''')
    # p[0] = p[1]
    pass

### ----------------------------------- Term
def p_term_multp(p):
    ''' term : term OP_MULTIPLICACION factor '''
    if log:
        print(''' term : term OP_MULTIPLICACION factor ''')
    # p[0] = p[1] * p[3]
    pass
    
def p_term_div(p):
    ''' term : term OP_DIVISION factor '''
    if log:
        print(''' term : term OP_DIVISION factor ''')
    # p[0] = p[1] / p[3]
    pass
    
def p_term(p):
    ''' term : factor '''
    if log:
        print(''' term : factor ''')
    # p[0] = p[1]
    pass
    
### ----------------------------------- Factor
def p_factor_num(p):
    ''' factor : CTE_NUMERICA '''
    if log:
        print(''' factor : CTE_NUMERICA ''') 
    # p[0] = p[1]
    pass
    
def p_factor_real(p):
    ''' factor : CTE_REAL '''
    if log:
        print(''' factor : CTE_REAL ''') 
    # p[0] = p[1]
    pass
    
def p_factor_id(p):
    ''' factor : ID ''' 
    if log:
        print(''' factor : ID ''' )
    # p[0] = p[1]
    pass
    
def p_factor_expression(p):
    ''' factor : PARENTESIS_ABRE expression PARENTESIS_CIERRA ''' 
    if log:
        print(''' factor : PARENTESIS_ABRE expression PARENTESIS_CIERRA ''' )
    pass


## ------------------------------ String Expression
def p_str_expression_concat(p):
    ''' str_expression : str_term OP_CONCAT str_term '''
    if log:
        print(''' str_expression : str_term OP_CONCAT str_term ''')
    pass

def p_str_expression(p):
    ''' str_expression : str_term '''
    if log:
        print(''' str_expression : str_term ''')
    pass

def p_str_term_cte(p):
    ''' str_term : CTE_STRING '''
    if log:
        print(''' str_term : CTE_STRING ''')
    # p[0] = p[1]
    pass
    
def p_str_term_id(p):
    ''' str_term : ID '''
    if log:
        print(''' str_term : ID ''')
    # p[0] = p[1]
    pass


## ------------------------------ Comparision Operations
def p_comparision(p):
    ''' comparision : expression op_comparision expression '''
    if log:
        print(''' comparision : expression op_comparision expression ''')
    pass

def p_comparision_str(p):
    ''' comparision : str_expression op_comparision str_expression '''
    if log:
        print(''' comparision : str_expression op_comparision str_expression ''')
    pass

### ----------------------------------- Comparision Operators
def p_op_comparision_minor(p):
    ''' op_comparision : COMP_MENOR '''
    if log:
        print(''' op_comparision : COMP_MENOR ''')
    pass

def p_op_comparision_major(p):
    ''' op_comparision : COMP_MAYOR '''
    if log:
        print(''' op_comparision : COMP_MAYOR ''')
    pass

def p_op_comparision_minor_eq(p):
    ''' op_comparision : COMP_MENOR_IGUAL '''
    if log:
        print(''' op_comparision : COMP_MENOR_IGUAL ''')
    pass

def p_op_comparision_major_eq(p):
    ''' op_comparision : COMP_MAYOR_IGUAL '''
    if log:
        print(''' op_comparision : COMP_MAYOR_IGUAL ''')
    pass

def p_op_comparision_equal(p):
    ''' op_comparision : COMP_IGUAL '''
    if log:
        print(''' op_comparision : COMP_IGUAL ''')
    pass

def p_op_comparision_distinct(p):
    ''' op_comparision : COMP_DISTINTO '''
    if log:
        print(''' op_comparision : COMP_DISTINTO ''')
    pass


## ------------------------------ Logical Expressions
### ----------------------------------- Logical Statement
def p_logical_statement(p):
    ''' logical_statement : logical_expression '''
    if log:
        print(''' logical_statement : logical_expression ''')
    pass

def p_logical_statement_with_operators(p):
    ''' logical_statement : logical_expression op_logic logical_expression '''
    if log:
        print(''' logical_statement : logical_expression op_logic logical_expression ''')
    pass

### ----------------------------------- Logical Expression
def p_logical_expression_not(p):
    ''' logical_expression : OP_NOT logical_term '''
    if log:
        print(''' logical_expression : OP_NOT logical_term ''')
    pass

def p_logical_expression(p):
    ''' logical_expression : logical_term '''
    if log:
        print(''' logical_expression : logical_term ''')
    pass

### ----------------------------------- Logical Term
def p_logical_term_comparision(p):
    ''' logical_term : comparision '''
    if log:
        print(''' logical_term : comparision ''')
    pass

def p_logical_term_between(p):
    ''' logical_term : between_statement '''
    if log:
        print(''' logical_term : between_statement ''')
    pass

def p_logical_term_cte(p):
    ''' logical_term : cte_logic '''
    if log:
        print(''' logical_term : cte_logic ''')
    pass

### ----------------------------------- Logical Operators
def p_op_logic_or(p):
    ''' op_logic : OP_OR '''
    if log:
        print(''' op_logic : OP_OR ''')
    pass

def p_op_logic_and(p):
    ''' op_logic : OP_AND '''
    if log:
        print(''' op_logic : OP_AND ''')
    pass

### ----------------------------------- Logical Constants
def p_cte_logic_true(p):
    ''' cte_logic : true '''
    if log:
        print(''' cte_logic : true ''')
    pass

def p_cte_logic_false(p):
    ''' cte_logic : false '''
    if log:
        print(''' cte_logic : false ''')
    pass

### ----------------------------------- Between Statement
def p_between_statement(p):
    ''' between_statement : between PARENTESIS_ABRE ID COMA expression DOS_PUNTOS expression PARENTESIS_CIERRA '''
    if log:
        print(''' between_statement : between PARENTESIS_ABRE ID COMA expression DOS_PUNTOS expression PARENTESIS_CIERRA ''')
    pass


## ------------------------------ Assignment Statement
def p_assignment_statement(p):
    ''' assignment_statement : ID OP_ASIGNACION assignment_value PUNTO_COMA '''
    if log:
        print(''' assignment_statement : ID OP_ASIGNACION assignment_value PUNTO_COMA ''')
    pass

def p_assignment_value_ternary(p):
    ''' assignment_value : ternary '''
    if log:
        print(''' assignment_value : ternary ''')
    pass

def p_assignment_value_expression(p):
    ''' assignment_value : expression '''
    if log:
        print(''' assignment_value : expression ''')
    pass

def p_assignment_value_str(p):
    ''' assignment_value : str_expression '''
    if log:
        print(''' assignment_value : str_expression ''')
    pass

def p_assignment_value_logical(p):
    ''' assignment_value : logical_statement '''
    if log:
        print(''' assignment_value : logical_statement ''')
    pass

### ----------------------------------- Ternary Operator
def p_ternary_num(p):
    ''' ternary : logical_statement CONDICION_TERNARIA expression DOS_PUNTOS expression '''
    if log:
        print(''' ternary : logical_statement CONDICION_TERNARIA expression DOS_PUNTOS expression ''')
    pass

def p_ternary_str(p):
    ''' ternary : logical_statement CONDICION_TERNARIA str_expression DOS_PUNTOS str_expression '''
    if log:
        print(''' ternary : logical_statement CONDICION_TERNARIA str_expression DOS_PUNTOS str_expression ''')
    pass


## ------------------------------ Error Rule
def p_error(e):
    print(f"\n[ERROR: ${e}]\n")


def parse(source):
    parser = yacc.yacc()  
    res = parser.parse(input=source, lexer=lexico.Lexer())
    if res is None:
        print("PARSING ERROR")
        return None
    return res