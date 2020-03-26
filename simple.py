def merge(p, r, newArr):
    nL = len(p)
    nR = len(r)
    i = j = k = 0

    while nL > i and nR > j:

        if p[i] <= r[j]:
            newArr[k] = p[i]
            i += 1
            k += 1
        else:
            newArr[k] = r[j]
            j += 1
            k += 1

    while i < nL:
        newArr[k] = p[i]
        i += 1
        k += 1

    while j < nR:
        newArr[k] = r[j]
        j += 1
        k += 1


def mergeSort(arr):
    a = len(arr)

    if a <= 1:
        return
    mid = int(a / 2)

    p = []
    r = []

    for i in range(mid):
        p.append(arr[i])

    for i in range(mid, a):
        r.append(arr[i])

    mergeSort(p)
    mergeSort(r)
    merge(p, r, arr)


arr = [56, 2, 21, 24, 1, 89, 0, 6]
mergeSort(arr)

for i in arr:
    print(i)
