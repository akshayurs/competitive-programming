# sub array of length k with minimum difference between smallest and largest elements
# all test cases passed gfg
def min_diff(arr, n, m):
    arr.sort()
    min_ = arr[n-1]-arr[0]
    for i in range(n-m+1):
        min_ = min(min_, arr[i+m-1]-arr[i])
    return min_


arr = [3, 4, 1, 9, 56, 7, 9, 12]
n = len(arr)
m = 5
print(min_diff(arr, n, m))  # 6
