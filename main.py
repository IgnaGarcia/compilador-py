import sys
from parser import sintactico
from assembly import asembler

debug = True

def main(path):
    with open(path) as source:
        print("Comienzo de Compilacion...")
        data = source.read()  
        polaca = sintactico.parse(data)
        asembler.run(polaca)
    source.close()
    print("...Fin de Compilacion")
    

if __name__ == "__main__":
    if(len(sys.argv) > 2 and sys.argv[2] == '-s'):
        with open('out/out.txt', 'w') as f:
            sys.stdout = f # Comentar para ver los logs
            main(sys.argv[1])
    else: main(sys.argv[1])
