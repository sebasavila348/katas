import sys

if len(sys.argv) == 3:
    fil = int(sys.argv[1])
    col = int(sys.argv[2])
    
    if 0 < fil < 10 and 0 < col < 10 :
        
        for f in range(fil):

            for c in range(col):
                print(" * ", end='')
            
            print("")

    
    else:
        print("Error, debe ser numeros enteros menores que 10 y mayores que 10")

else:
    print("Error, el script debe recibir 2 argumentos")
    print("Ejemplo: ruta 5 4")