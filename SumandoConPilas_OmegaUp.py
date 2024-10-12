num = int(input())
cont = 0
l = []
while cont < num :
    entrada = input()
    opc = entrada.split()
    if len(opc) == 2:       
        l.append(int(opc[1]))
    elif opc[0] == "IMPRIME":
        print(l[len(l)-1])
    else:
        a = l.pop()
        b = l.pop()
        l.append(a+b)
    cont +=1