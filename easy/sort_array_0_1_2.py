# sort the array containing 0,1,2
# All test cases passed GFG

def sortArray(arr, n):

    low = -1  # 0 index to low - 0
    mid = 0  # low to mid - 1 ,  mid to high unknown
    high = n  # high to n - 2
    while mid < high:
        if arr[mid] == 0:
            low += 1
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            high -= 1
            arr[mid], arr[high] = arr[high], arr[mid]

    return arr


print(sortArray([0, 2, 1, 0, 0, 1], 6))
print(sortArray([2, 2, 2, 0, 0, 0, 1, 1, 1], 9))
print(sortArray([2, 1, 0, 0, 1, 2, 2, 0, 1], 9))
print(sortArray([0, 0, 1, 1, 2, 2], 4))
