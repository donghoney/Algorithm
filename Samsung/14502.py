import sys

n, m = map(int, sys.stdin.readline().split())
virus_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
virus_arr = []
for i in range(n):
    for j in range(m):
        if virus_map[i][j] == 2:
            virus_arr.append([i, j])


def bfs():
    global max_ans, n, m
    copy_map = [[0]*m for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            copy_map[i][j] = virus_map[i][j]

    for vi_row, vi_col in virus_arr:
        q = [[vi_row, vi_col]]
        while q:
            a = q.pop()
            for i in range(4):
                ax = a[0] + dx[i]
                by = a[1] + dy[i]
                if 0 <= ax < n and 0 <= by < m and copy_map[ax][by] == 0:
                    copy_map[ax][by] = 2
                    q.append([ax, by])

    for i in range(n):
        for j in range(m):
            if copy_map[i][j] == 0:
                res += 1
    max_ans = max(max_ans, res)


def dfs(cnt, x, y):
    if cnt == 3:
        bfs()
        return

    for i in range(x, n):
        for j in range(y, m):
            if virus_map[i][j] == 0:
                virus_map[i][j] = 1
                dfs(cnt+1, x, y+1)
                virus_map[i][j] = 0
        y = 0

dfs(0, 0, 0)
print(max_ans)