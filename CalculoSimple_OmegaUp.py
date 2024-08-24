entrada = input()
suma = 0
entrada2 = input()
lista = list(map(float, entrada.split()))
suma += lista[1] * lista[2]
list2 = list(map(float,entrada2.split()))
suma += list2[1] * list2[2]
print("{:.2f}".format(suma))
