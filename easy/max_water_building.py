# maximum water can be filled between the buildings

def maxWater(arr, n):
    maxL = left = 0
    maxR = right = n-1
    maxArea = 0
    while(left < right):
        newArea = min(arr[left], arr[right])*(right-left)
        if newArea > maxArea:
            maxL = left
            maxR = right
            maxArea = newArea
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    print(maxArea, maxL, maxR)


maxWater([1, 8, 6, 2, 5, 4, 8, 3, 7], 9)  # maxArea = 48 maxL = 1 maxR = 8
