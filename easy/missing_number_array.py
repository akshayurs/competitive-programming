# All test cases passed GFG

# arr - array of integers , n - length of array
def missingNumber(arr, n):
    neededSum = (n+1)*(n+2)/2
    realSum = sum(arr)
    return int(neededSum - realSum)


print(missingNumber([1, 2, 3, 5], 4))
