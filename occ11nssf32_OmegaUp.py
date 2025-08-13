nums = input()
numA, numB = nums.split()

max_len = max(len(numA), len(numB))
numA = numA.zfill(max_len)
numB = numB.zfill(max_len)

acarreo = 0
nAcarreos = 0

for i in range(max_len - 1, -1, -1): 
    suma = int(numA[i]) + int(numB[i]) + acarreo
    if suma >= 10:
        nAcarreos += 1
        acarreo = 1
    else:
        acarreo = 0
print(nAcarreos)