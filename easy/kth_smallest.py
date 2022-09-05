# O(klogn)
def heapify(arr, n, i):
    heap = False
    smallest = i
    left = 2*i+1
    right = 2*i+2
    if(left < n and arr[left] < arr[smallest]):
        smallest = left
    if(right < n and arr[right] < arr[smallest]):
        smallest = right
    if(smallest != i):
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def kthsmallest(arr, n, k):
    for i in range(int(n/2)-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, k-1, -1):
        heapify(arr, i, 0)
        arr[i], arr[0] = arr[0], arr[i]
    return arr[n-k]


arr = [6, 2, 4, 1, 5, 7]
n = len(arr)
k = 3
print(kthsmallest(arr, n, k))  # 4
