# O(klogn)
# all test cases pass InterviewBit
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
    n1 = n
    for i in range(k):
        n1 = n1-1
        arr[n1], arr[0] = arr[0], arr[n1]
        heapify(arr, n1, 0)
    return arr[n-k]


arr = [7, 10, 4, 20, 15]
n = len(arr)
k = 4
print(kthsmallest(arr, n, k))  # 15
