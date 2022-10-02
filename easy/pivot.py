# Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.
# All test cases passed GFG

def find_pivot(arr, n):
    lmax = [None]*(n)
    rmin = [None]*(n)
    temp = arr[0]
    for i in range(n):
        temp = max(temp, arr[i])
        lmax[i] = temp
    temp = arr[n-1]
    for i in range(n-1, -1, -1):
        temp = min(temp, arr[i])
        rmin[i] = temp
    for i in range(1, n-1):
        if arr[i] >= lmax[i-1] and arr[i] <= rmin[i+1]:
            return arr[i]
    return -1


arr = [4, 2, 5, 7]
n = len(arr)
print(find_pivot(arr, n))
