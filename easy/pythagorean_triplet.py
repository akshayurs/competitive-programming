# return true if triplet(a,b,c) from array satisfies a^2+b^2=c^2
# all test case passed gfg
def check_triplet(arr, n):
    set_arr = set()
    for i in arr:
        set_arr.add(i*i)
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]*arr[i] + arr[j]*arr[j]) in set_arr:
                return True
    return False


arr = [1, 2, 3]
print(check_triplet(arr, len(arr)))  # False
