
def rotateArrayLeft(arr, n, d):
    return arr[d:]+arr[:d]


def rotateArrayRight(arr, n, d):
    return arr[n-d:]+arr[:n-d]


print(rotateArrayLeft([1, 2, 3, 4, 5], 5, 2))
print(rotateArrayRight([1, 2, 3, 4, 5], 5, 2))
