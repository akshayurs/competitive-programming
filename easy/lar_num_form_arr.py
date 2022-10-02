# Given a list of non negative integers, arrange them in such a manner that they form the largest number possible
# GFG Time exceed
def lar_num(arr, n):
    arr = [str(i) for i in arr]
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j] < arr[j] + arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return "".join(arr)


arr = [3, 30, 34, 5, 9]
n = len(arr)
print(lar_num(arr, n))
