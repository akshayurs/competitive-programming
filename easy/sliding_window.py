# maximum sum with k consecutive elements in array


def maxSum(arr, k):
    sum = 0
    index = 0
    for i in range(k):
        sum += arr[i]
    ans = sum
    for i in range(k, len(arr)):
        sum = sum + arr[i] - arr[i-k]
        if ans < sum:
            ans = sum
            index = i-k + 1
    return [ans, index]


print(maxSum([2, 1, 5, 2, 3, 1, 8], 3))  # [12,4]
print(maxSum([80, -50, 90, 100], 2))  # [190,2]
