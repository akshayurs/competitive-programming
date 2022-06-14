# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.
# All test cases passed GFG

def subArrayWithSum(arr, n, requiredSum):
    currentSum = arr[0]
    start = 0
    end = 0
    for i in range(1, n+1):
        while(currentSum > requiredSum):
            currentSum -= arr[start]
            start += 1
        if currentSum == requiredSum:
            return (start, end)
        if i < n:
            currentSum += arr[i]
        end += 1
    return


print(subArrayWithSum([1, 2, 3, 4, 5], 5, 9))  # (1,3)
