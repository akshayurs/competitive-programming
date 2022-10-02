# print arr in the form - arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]

def zigzag(arr, n):
    flag = False
    for i in range(n-1):
        if flag == True:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = not flag
    return arr


arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
print(zigzag(arr, n))  # [3, 7, 4, 8, 2, 6, 1]   => 3 < 7 > 4 < 8 > 2 < 6 > 1
