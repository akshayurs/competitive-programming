
def rotateArrayAntiClock(arr, n, d):
    return arr[d:]+arr[:d]


def rotateArrayClock(arr, n, d):
    return arr[n-d:]+arr[:n-d]


print(rotateArrayAntiClock([1, 2, 3, 4, 5], 5, 2))
print(rotateArrayClock([1, 2, 3, 4, 5], 5, 2))
