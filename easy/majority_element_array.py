# Element which appears more than len/2 times in array
# All test cases passed Leet code
def majorityELement(arr, n):
    majority = arr[0]
    count = 0
    for ele in arr:
        if ele == majority:
            count += 1
        else:
            count -= 1
        if count <= 0:
            count = 1
            majority = ele
    count = 0
    for ele in arr:
        if majority == ele:
            count += 1
    if count > n/2:
        return majority
    return


print(majorityELement([3, 3, 4, 2, 4, 4, 2, 4, 4], 9))  # 4
print(majorityELement([3, 3, 4, 2, 4, 4, 2, 4], 8))  # None
print(majorityELement([1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2], 13))  # 1
