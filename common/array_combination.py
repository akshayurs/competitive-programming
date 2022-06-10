# To get all possible array combinations of length k
#
# combination(Array arr,int length)
#
# Example :
# arr = [1,2,3] k = 2
# combination([1,2,3],2)
# [[1, 2], [1, 3], [2, 3]]


# combination_calc(Array arr, int n, Array cur, int k, Array ans)
# arr is original input array, length - > len(remaining array), cur is the possible combinations formed by original array
def combination_calc(arr, n, cur, k, ans):
    if k == 0:
        ans.append(cur)
        return
    for i in range(n):
        # arr[i+1:] is remaining array from i+1 th index of original array
        combination_calc(arr[i+1:], n-i-1, cur+[arr[i]], k-1, ans)


def combination(arr, k):
    ans = []
    combination_calc(arr, len(arr), [], k, ans)
    return ans


# Example
print(combination([1, 2, 3], 2))
# [[1, 2], [1, 3], [2, 3]]
