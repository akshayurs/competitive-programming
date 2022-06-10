# To get all possible array permutations of length k
#
# permutation(Array arr,int length)
#
# Example :
# arr = [1,2,3] k = 2
# permutation([1,2,3],2)
# [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]]


# permutation_calc(Array arr, int n, Array cur, int k, Array ans)
# arr is original input array, length - > len(remaining array), cur is the possible permutations formed by original array
def permutation_calc(arr, n, cur, k, ans):
    if k == 0:
        ans.append(cur)
        return
    for i in range(n):
        # arr[i:] is remaining array without ith value in original array
        permutation_calc(arr[:i]+arr[i+1:], n-1, cur+[arr[i]], k-1, ans)


def permutation(arr, k):
    ans = []
    permutation_calc(arr, len(arr), [], k, ans)
    return ans


# Example
print(permutation([1, 2, 3], 2))
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
