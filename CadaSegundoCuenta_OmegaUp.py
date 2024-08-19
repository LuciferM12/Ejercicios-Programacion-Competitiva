
hora1 = input()
hora1 = hora1.replace(" ", "")
hora1 = list(map(int, hora1.split(":")))

hora2 = input()
hora2 = hora2.replace(" ", "")
hora2 = list(map(int, hora2.split(":")))

segundos1 = hora1[0] * 3600 + hora1[1] * 60 + hora1[2]
segundos2 = hora2[0] * 3600 + hora2[1] * 60 + hora2[2]

diferencia = abs(segundos2 - segundos1)

if segundos1 > segundos2:
    diferencia = 86400 - diferencia

print(diferencia)
