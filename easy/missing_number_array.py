def missingNumber(arr, n):
    neededSum = (n+1)*(n+2)/2
    realSum = sum(arr)
    return int(neededSum - realSum)


print(missingNumber([2, 3, 4, 5], 4))
