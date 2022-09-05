def find_equilibrium(arr, n):
    mid = int(n/2)
    leftSum = 0
    rightSum = 0
    for i in range(0, mid):
        leftSum += arr[i]
    for i in range(mid+1, n):
        rightSum += arr[i]
    if(rightSum > leftSum):
        while(rightSum > leftSum and mid < n-1):
            rightSum -= arr[mid+1]
            leftSum += arr[mid]
            mid += 1
    elif (leftSum > rightSum):
        while(rightSum < leftSum and mid > 0):
            rightSum += arr[mid]
            leftSum -= arr[mid-1]
            mid -= 1
    if(rightSum == leftSum):
        return mid
    else:
        return -1


print(find_equilibrium([1, 3, 5, 2, 2], 5))
print(find_equilibrium([1], 1))
