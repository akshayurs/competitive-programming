# To get all possible string combinations with length k
#
# possibility(String str,int length)
#
# Example :
# string = 'abc' k = 2
# possibility('abc',2)
# ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

# possibility_calc(Array, int , Array, int , Array)
# arr is original input array, length - > len(original array), cur is the possible value formed by original array
def possibility_calc(arr, length, cur, k, ans):
    if k == 0:
        # ans.append(cur) to append array.here joining letters to form string ,because cur is array of char for string
        ans.append("".join(cur))
        return
    for i in range(length):
        possibility_calc(arr, length, cur+[arr[i]], k-1, ans)


def possibility(arr, k):
    ans = []
    possibility_calc(arr, len(arr), [], k, ans)
    return ans


# Example
print(possibility("abc", 2))
# ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
