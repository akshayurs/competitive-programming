# Maximum length of substring without repeating char
# All test cases passes GFG

def check_substring(string, n):
    # last occurrence of the character
    char_map = {}
    # substring
    maxL = left = 0
    maxR = right = 0
    maxLength = 1

    for i in range(n):
        if string[i] in char_map:
            left = max(left, char_map[string[i]]+1)
        char_map[string[i]] = i
        right += 1
        if maxLength < right-left:
            maxLength = right-left
            maxL = left
            maxR = right
    return (maxL, maxR, maxLength)


print(check_substring("aabcabcbb", 9))  # index (1,4) length 3
