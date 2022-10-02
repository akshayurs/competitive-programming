# Print matrix elements spirally
# all test case passed gfg

def spiral_mat(arr, m, n):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    di = 0
    ans = []
    seen = [[0 for i in range(n)] for j in range(m)]
    x, y = 0, 0
    for i in range(m*n):
        ans.append(arr[x][y])
        seen[x][y] = 1
        cr = x + dr[di]
        cc = y + dc[di]
        if (cr >= 0 and cr < m and cc >= 0 and cc < n and not seen[cr][cc]):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x = x + dr[di]
            y = y + dc[di]
    return ans


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
m = len(arr)
n = len(arr[0])
print(spiral_mat(arr, m, n))
# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
