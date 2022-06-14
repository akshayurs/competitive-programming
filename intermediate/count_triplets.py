#  Time limit exceeded in GFG (Even for standard GFG solution)

def countTriplets(arr, n):
    ans = 0
    maxValue = max(arr)

    freq = [0 for i in range(maxValue+1)]

    for i in arr:
        freq[i] += 1

    # Case 1 (0,0,0)
    # freq[0] Combination 3  = freq(0)C3 = freq(0)!/((freq(0)-3)*3!)
    ans += (freq[0]*(freq[0]-1)*(freq[0]-2)//6)

    # Case 2 (0,x,x)
    # freq(0)*freq(2)C2
    for i in range(maxValue+1):
        ans += (freq[0]*freq[i]*(freq[i]-1)//2)

    # Case 3 (x,x,2x)
    for i in range(1, (maxValue + 1) // 2):
        ans += (freq[i] * (freq[i] - 1) // 2 * freq[2 * i])

    # Case 4 (x,y,x+y)
    for i in range(1, maxValue+1):
        for j in range(i+1, maxValue-i+1):
            ans += freq[i] * freq[j] * freq[i + j]

    return ans


print(countTriplets([1, 2, 3, 4, 5], 5))
