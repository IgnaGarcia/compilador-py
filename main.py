import sys
from lex import lexico

def main(path):
    with open(path) as f:
        while True:
            character = f.read(1)
            print(character)
            
            if not character:
                print("End of file")
                break
            
            response = lexico.main()
            
            if not response["ok"]:
                print("Error en Lexico")
                break
            
            print(response["token"])
            
    f.close()
    

if __name__ == "__main__":
    main(sys.argv[1])