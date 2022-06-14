# merge two sorted array
# All test cases passed GFG

def merge(A, B, m, n):
    C = []
    i, j = 0, 0
    while(i < m and j < n):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i != m:
        while(i < m):
            C.append(A[i])
            i += 1
    else:
        while(j < n):
            C.append(B[j])
            j += 1
    return C


# print(merge([1, 2, 3, 4], [5, 6], 4, 2))
# print(merge([6, 7], [1, 2, 3, 4, 5], 2, 5))
# print(merge([4, 5], [1, 3, 5, 7], 2, 5))
print(merge([1, 3, 5, 7], [0, 2, 4, 6, 8], 4, 5))
