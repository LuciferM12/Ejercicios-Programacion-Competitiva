entrada = input()
numeros = list(map(int, entrada.split()))
resp = [True, True, True, True, True]
if numeros[0] >= numeros[1]:
    resp[0] = False
if numeros[2] < numeros[0]:
    resp[1] = False
if numeros[0] != numeros[1]:
    resp[2] = False
if numeros[0] == numeros[2]:
    resp[3] = False
if numeros[2] >= numeros[1]:
    resp[4] = False
for i in range (len(resp)):
    print(resp[i], end=" ")
