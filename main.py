import sys
from parser import sintactico

def main(path):
    with open(path) as source:
        data = source.read()  
        sintactico.parse(data)
    source.close()
    

if __name__ == "__main__":
    with open('out/out.txt', 'w') as f:
        #sys.stdout = f # Comentar para ver los logs
        main(sys.argv[1])