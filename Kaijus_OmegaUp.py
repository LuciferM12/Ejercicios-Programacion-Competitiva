jaegers = int(input())
cont = 0
while True:
    if jaegers < 2**cont:
        break
    else:
        cont+=1
print(2018+cont)