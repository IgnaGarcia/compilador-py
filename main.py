import sys
from parser import sintactico

def main(path):
    with open(path) as source:  
        sintactico.parse(source)
        '''
        while True:
            character = source.read(1)
            
            if not character:
                print("End of file")
                break
            
            response = lexico.yylex(source, character)
            
            if not response["ok"]:
                print(f"[Error en Lexico]: {response['token']}")
                break
            
            print("[TOKEN]: ", response["token"])
        ''' 
    source.close()
    

if __name__ == "__main__":
    main(sys.argv[1])