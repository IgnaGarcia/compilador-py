def open_file(input):
    source = open(input)
    # with open(input) as source:
    #     while True:
    #         char = source.read(1)
    #         if not char:
    #             break
    #         print(char)
    return source

def close_file(source):
    source.close()
    return

def get_event(char):
    if char >= 'A' and char <= 'Z': return 0
    if char >= 'a' and char <= 'z': return 0
    if char >= 0 and char <= 9: return 1
    if char == '""': return 3
    if char == '{': return 4
    if char == '}': return 5
    if char == '(': return 6
    if char == ')': return 7
    if char == '.': return 8
    if char == ';': return 9
    if char == ',': return 10
    if char == '-': return 11
    if char == '+': return 12
    if char == '/': return 13
    if char == '*': return 14
    if char == '<': return 15
    if char == '<': return 16
    if char == '>': return 17
    if char == '|': return 18
    if char == '&': return 19
    if char == '!': return 20
    if char == '=': return 21
    if char == ':': return 22
    if char == '?': return 23
    if char == ' ': return 24
    if char == '/t': return 24
    if char == '/n': return 24
    if char == '/r': return 24

# open_file("source.txt")
print(get_event("1")) 

