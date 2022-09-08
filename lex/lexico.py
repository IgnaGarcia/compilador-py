from lex import process_table as pt, states_table as st, token_table as tt, keyword_table as kt

def get_event(char):
    if char >= 'A' and char <= 'Z': return 0
    if char >= 'a' and char <= 'z': return 0
    if char >= '0' and char <= '9': return 1
    if char == '"': return 2
    if char == '{': return 3
    if char == '}': return 4
    if char == '(': return 5
    if char == ')': return 6
    if char == '.': return 7
    if char == ';': return 8
    if char == ',': return 9
    if char == '-': return 10
    if char == '+': return 11
    if char == '/': return 12
    if char == '*': return 13
    if char == '<': return 14
    if char == '<': return 15
    if char == '>': return 16
    if char == '|': return 17
    if char == '&': return 18
    if char == '!': return 19
    if char == '=': return 20
    if char == ':': return 21
    if char == '?': return 22
    if char == ' ': return 23
    if char == '\t': return 23
    if char == '\n': return 23
    if char == '\r': return 23
    if char == '': return 23

def yylex(source, char):
    state = 0
    final_state = -1
    error_state = -2
    
    while state is not final_state:
        column = get_event(char)
        
        response = pt.process_table[state][column](char)
        
        last = state
        state = st.next_state[state][column]
        
        if state == error_state:
            return { "ok": false, "token": f"Caracter {char} no esperado" }
        
        char = source.read(1)
        print(char)
        if state == final_state:
            token = tt.get_token_label(last, column)
            if token == 256 or token == "ID":
                token = kt.keyword_token_label(response)
            break
               
    return { "ok": True, "token": token }