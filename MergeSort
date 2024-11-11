def Merge(arrl, arrr):
    resp = []
    while len(arrl) > 0 and len(arrr) > 0:
        if arrl[0] < arrr[0]:
            resp.append(arrl[0])
            arrl.pop(0)
        else:
            resp.append(arrr[0])
            arrr.pop(0)
    if len(arrr) > 0:
        resp += arrr
    if len(arrl) > 0:
        resp += arrl
    return resp

def mergeOrder(arr):
    if len(arr) == 1:
        return arr
    mitad = arr//2
    leftarr = arr[mitad:]
    rightarr = arr[:mitad]
    sortl = mergeOrder(leftarr)
    sortr = mergeOrder(rightarr)
    return Merge(sortl, sortr)
