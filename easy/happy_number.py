# Happy number - Sum of squares of digits recursively comes to one

# false condition - getting sum which is already occurred
# All test cases passed Leet code

def happyNumber(n):
    sums = set()
    sums.add(n)
    while(1):
        sum = 0
        while(n != 0):
            sum += pow(n % 10, 2)
            n = int(n/10)

        if sum == 1:
            return True

        if sum in sums:
            return False

        n = sum
        sums.add(sum)


# True  82 => 8^2+2^2 = 64 + 4 = 68 => 6^2 + 8^2 = 36 + 64 = 100 => 1^2 + 0^2 + 0^2 = 1
print(happyNumber(82))

# False 61 => 6^2 +1^2 = 36 + 1 = 37 => 3^2 + 7^2 = 9 + 49 = 58 => 5^2 + 8^2 = 25 + 64 = 89 => 8^2 + 9^2 = 64 + 81 = 145 => 1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42 .....
print(happyNumber(61))
