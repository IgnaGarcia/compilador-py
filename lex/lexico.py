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
    if (char >= 'A' and char <= 'Z'): return 0
    if (char >= 'a' and char <= 'z'): return 0

# open_file("source.txt")
print(get_event("1")) 

