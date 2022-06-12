# Element which appears more than len/2 times in array
def majorityELement(arr, n):
    majority = arr[0]
    count = 0
    for ele in arr:
        if ele == majority:
            count += 1
        else:
            count -= 1
        if count <= 0:
            count = 0
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
