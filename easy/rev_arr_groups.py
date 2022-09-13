# reverse array elements in group of k
# all test case passed gfg
def reverse_groups(arr, n, k):
    for i in range(0, n, k):
        left = i
        right = min(i+k-1, n-1)
        while(left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
k = 4

print(reverse_groups(arr, n, k))
