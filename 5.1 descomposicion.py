import sys

if len(sys.argv) == 2:

    cadena = sys.argv[1]
    c_inver = cadena[::-1]

    lista = list(map(int,c_inver))
    lista

    for i,v in enumerate(lista):
        print(f"{v*10**i:0{len(lista)}d}")
    

    

else:
    print("Error, el script debe recibir 1 argumento")
    print("Ejemplo: 334")