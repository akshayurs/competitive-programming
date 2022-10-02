# Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
# All test cases passed GFG
def trappingWater(arr, n):
    rightmax = []
    max = 0
    ans = 0
    curMax = 0
    for i in range(n-1, -1, -1):
        if arr[i] > max:
            max = arr[i]
        rightmax.append(max)
    for i in range(n):
        if arr[i] > curMax:
            curMax = arr[i]

        ans += min(curMax, rightmax[n-1-i])-arr[i]
    return ans


print(trappingWater([]))
