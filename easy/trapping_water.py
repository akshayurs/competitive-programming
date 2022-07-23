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
