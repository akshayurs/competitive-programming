# all test case passed gfg
def romanToDecimal(S):
    val = {"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000,
           }
    ans = val[S[0]]
    n = len(S)
    neg = False
    for i in range(1, n):
        if val[S[i-1]] < val[S[i]]:
            neg = True
        if neg:
            # ans = val[S[i]]-ans
            ans = ans + val[S[i]] - 2*val[S[i-1]]
        else:
            ans = ans + val[S[i]]
        neg = False
    return ans


print(romanToDecimal("V"))  # 5
print(romanToDecimal("IV"))  # 4
print(romanToDecimal("CMXVI"))  # 916
print(romanToDecimal("XXIII"))  # 23
print(romanToDecimal("MMMDCCXCIV"))  # 3794
print(romanToDecimal("CXIV"))  # 114
