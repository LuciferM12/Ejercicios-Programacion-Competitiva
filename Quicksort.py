def partition(array, low, high):
    pivote = array[high]
    i = low -1
    for j in range(low, high):
        if array[j] <= pivote:
            i+=1
            (array[j], array[i]) = (array[i], array[j])
    (array[high], array[i+1]) = (array[i+1], array[high])
    return i+1


def quicksort(array, low, high):
    if high > low:
        pi = partition(array, low, high)

        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
