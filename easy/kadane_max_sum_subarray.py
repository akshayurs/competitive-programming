# maximum sum contiguous sub array
# kadane's algorithm
def kadane(arr, n):
    max_global = arr[0]
    max_current = arr[0]
    max_start = start = 0
    max_end = end = 0

    for i in range(1, n):
        # either include ith ele with prev sub array or consider only ith ele
        if arr[i] > arr[i]+max_current:
            max_current = arr[i]
            start = i
            end = i
        else:
            max_current += arr[i]
            end = i
        if max_current > max_global:
            max_global = max_current
            max_start = start
            max_end = end
    return (max_global, max_start, max_end)


print(kadane([-2, -3, 4, -1, -2, 1, 5, -3], 8))
