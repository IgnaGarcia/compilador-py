keywords = {
    "while": 260,
    "if": 261,
    "else": 262,
    "between": 263,
    "out": 264,
    "in": 265,
    "var": 266,
    "string": 267,
    "int": 268,
    "real": 269,
    "bool": 293,
}

def keyword_token(id):
    if id in keywords:
        return keywords[id]
    return 0