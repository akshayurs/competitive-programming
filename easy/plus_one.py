def plusOne(arr, n):
    ans = []
    rem = 0
    arr[n-1] += 1
    for i in range(n-1, -1, -1):
        ans.insert(0, (arr[i]+rem) % 10)
        rem = (arr[i]+rem)//10
    if rem != 0:
        ans.insert(0, rem)
    return ans


print(plusOne([9, 9, 9, 9], 4))  # [1,0,0,0,0]
print(plusOne([7, 8, 3, 9], 4))  # [7,8,4,0]
