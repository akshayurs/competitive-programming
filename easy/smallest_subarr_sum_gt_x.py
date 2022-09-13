# Smallest sub array with sum greater than x
# all test cases passed gfg
def smallest_subarr_sum(arr, n, x):
    start = 0
    end = 0
    ans = n
    sum = arr[0]
    for i in range(1, n):
        end += 1
        sum += arr[i]
        while(sum - arr[start] > x):
            sum -= arr[start]
            start += 1
        if end-start + 1 < ans and sum > x:
            ans = end - start + 1
    return ans


arr = [6, 3, 4, 5, 4, 3, 7, 9]
n = len(arr)
x = 16
print(smallest_subarr_sum(arr, n, x))  # 3
