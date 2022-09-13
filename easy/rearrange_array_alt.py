# Rearrange Array Alternately
# all test case passed gfg
def rearrange(arr, n):
    minele = arr[0]
    mini = 0
    maxele = arr[0]
    maxi = n-1
    for i in range(n):
        if arr[i] < minele:
            minele = arr[i]
        if arr[i] > maxele:
            maxele = arr[i]
    maxele += 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] = arr[i] + arr[maxi] % maxele * maxele
            maxi -= 1
        else:
            arr[i] = arr[i] + arr[mini] % maxele * maxele
            mini += 1
    for i in range(n):
        arr[i] = int(arr[i]/maxele)
    return arr


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rearrange(arr, n))  # [5, 1, 4, 2, 3]
