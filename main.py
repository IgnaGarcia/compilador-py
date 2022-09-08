import sys
from lex import lexico

def main(path):
    cont = 5
    with open(path) as source:
        while True and cont is not 0:
            character = source.read(1)
            print(character)
            
            if not character:
                print("End of file")
                break
            
            response = lexico.yylex(source, character)
            source.seek(1)
            
            if not response["ok"]:
                print(f"[Error en Lexico]: {response['token']}")
                break
            cont = cont -1
            print(response["token"])
            
    source.close()
    

if __name__ == "__main__":
    main(sys.argv[1])