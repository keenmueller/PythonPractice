#https://brilliant.org/wiki/sorting-algorithms/#sorting-algorithms
#basically just trying to get in some coding practice in my free time

import random

def mergeSort(x):
    if len(x) < 2:
        return x
    results = []
    mid = len(x) // 2
    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            results.append(z[0])
            z.pop(0)
        else:
            results.append(y[0])
            y.pop(0)
    results += y
    results += z

    return results


def insertionSort(x):
    if len(x) == 0:
        return x

    results = []
    results.append(x[0])
    x.pop(0)
    while len(x) > 0:
        i = len(results) - 1
        while i >= 0:
            if x[0] > results[i]:
                results.insert(i + 1, x[0])
                x.pop(0)
                break
            elif i == 0:
                results = [x[0]] + results
                x.pop(0)
                break
            else:
                i -= 1
    return results


def bubbleSort(x):
    results = []
    while len(x) > 1:
        max = len(x) - 1
        for y in range(0, max):
            if x[y] > x[y + 1]:
                temp = x[y]
                x[y] = x[y + 1]
                x[y + 1] = temp
        results = [x[max]] + results
        x.pop(max)
    return [x[0]] + results


def quickSort(x):
    if len(x) < 2:
        return x
    smaller = []
    larger = []
    same = []

    rand = random.randint(0, len(x) - 1)
    pivot = x[rand]
    for y in x:
        if y < pivot:
            smaller.append(y)
        elif y > pivot:
            larger.append(y)
        else:
            same.append(y)

    return quickSort(smaller) + same + quickSort(larger)
