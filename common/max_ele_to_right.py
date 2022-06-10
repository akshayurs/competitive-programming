# Maximum element to the right of the element
def maxRight(arr, n):
    maxEle = arr[n-1]
    newArr = []
    for i in range(n-1, -1, -1):
        if arr[i] > maxEle:
            maxEle = arr[i]
        newArr.insert(0, maxEle)
    return newArr


print(maxRight([4, 2, 3, 1, 2], 5))
