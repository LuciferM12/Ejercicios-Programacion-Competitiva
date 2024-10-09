entrada = input()
numeros = list(map(int, entrada.split()))
cont = 0
while cont < numeros[0]:
    c = int(input())
    if c % numeros[1] == 0:
        if c % numeros[2] == 0:
            print("BIENMAL")
        else:
            print("BIEN")
    elif c % numeros[2] == 0:
        print("MAL")
    else:
        print("NORMAL")
    cont+=1
        
