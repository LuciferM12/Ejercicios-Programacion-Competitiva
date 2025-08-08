entrada = input()
c, p, h = map(int, entrada.split())
restantes = c - p
restantes = restantes%(h+1)
total = p + restantes
print(total)