import sys
from parser import sintactico

def main(path):
    with open(path) as source:
        data = source.read()  
        sintactico.parse(data)
    source.close()
    

if __name__ == "__main__":
    main(sys.argv[1])