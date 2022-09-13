# longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
# all test cases passed gfg
def long_cons_subseq(arr, n):
    ans = 0
    s = set(arr)
    for i in arr:
        if i-1 not in s:
            j = i
            while(j in s):
                j += 1
            ans = max(ans, j-i)
    return ans


arr = [2, 6, 9, 4, 5, 3, 7]
n = len(arr)
print(long_cons_subseq(arr, n))  # 6
