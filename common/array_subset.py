#  Array subsets

def subset_calc(arr, cur, ans):
    ans.append(cur)
    for index in range(len(arr)):
        if arr[index] not in cur:
            # arr[index:] is remaining array from index
            subset_calc(arr[index:], cur+[arr[index]], ans)


def subsets(arr):
    ans = []
    subset_calc(arr, [], ans)
    return ans


print(subsets([1, 2, 3]))
