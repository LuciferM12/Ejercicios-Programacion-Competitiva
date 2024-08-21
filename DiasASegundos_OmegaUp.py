import sys
datos = sys.stdin.read().splitlines()
for dato in datos:
    if dato != "":
        print(int(dato)*24*3600)