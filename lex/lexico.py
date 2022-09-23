from lex import process_table as pt, states_table as st, token_table as tt, keyword_table as kt

class LexToken(object):
    def __init__(self, type, value, lineno, lexpos):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.lexpos = lexpos
        
    def __str__(self):
        return 'LexToken(%s,%r,%d,%d)' % (self.type, self.value, self.lineno, self.lexpos)

    def __repr__(self):
        return str(self)

class Lexer: 
    def __init__(self):
        self.source = None
        

    def get_column(self, char):
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
        if char == '>': return 15
        if char == '|': return 16
        if char == '&': return 17
        if char == '!': return 18
        if char == '=': return 19
        if char == ':': return 20
        if char == '?': return 21
        if char == ' ': return 22
        if char == '\t': return 22
        if char == '\n': return 22
        if char == '\r': return 22
        if char == '': return 23
        

    def unread(self):
        cursor = self.source.tell()
        self.source.seek(cursor-1)
        
        
    def input(self, s):
        self.source = s
        

    def token(self):
        state = 0
        final_state = -1
        error_state = -2
        char = self.source.read(1)
        
        while state != final_state:
            column = self.get_column(char)
            
            response = pt.process_table[state][column](char)
            
            last = state
            state = st.next_state[state][column]
            
            if state == error_state:
                return None
            
            if state == final_state:
                token = tt.get_token_label(last, column)
                if token["type"] == "ID":
                    token = kt.keyword_token_label(response)
                if token["type"] in ["ID", "CTE_NUMERICA", "CTE_REAL", "CTE_STRING"]:
                    token["value"] = response
                print(token)
                break
            
            char = self.source.read(1)
                
        if column != 23:
            self.unread()
        return LexToken(token["type"], token["value"], 0, 0)