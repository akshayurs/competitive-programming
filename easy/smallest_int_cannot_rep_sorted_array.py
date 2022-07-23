# smallest integer that cannot be represented as sum of subset sorted array
# All test cases passes GFG
def smallestInt(arr):
    res = 1
    for i in arr:
        if i <= res:
            res += i
    return res


print(smallestInt([1, 1, 2, 5]))  # 10
print(smallestInt([7, 8, 9, 1]))  # 2
