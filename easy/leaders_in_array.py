#  An element of array is leader if it is greater than or equal to all the elements to its right side
# All test cases passes GFG

def leader(arr, n):
    ans = []
    maxEle = float("-inf")
    for i in range(n-1, -1, -1):
        if arr[i] >= maxEle:
            maxEle = arr[i]
            ans.append(maxEle)
    return ans[::-1]


print(leader([16, 17, 4, 3, 5, 2], 6))  # [17,5,2]
