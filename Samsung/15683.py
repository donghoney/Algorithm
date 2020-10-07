n, m = map(int, input().split())
cctv = [list(map(int, input().split())) for _ in range(n)]
dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
min_result = 1000000
arr = []

for i in range(n):
    for j in range(m):
        if 0 < cctv[i][j] < 6:
            arr.append([i, j])


def check():
    ans = 0
    for i in range(n):
        for j in range(m):
            if cctv[i][j] == 0:
                ans += 1
    return ans


def visible(i, di, row, col):
    ax = row + dx[di]
    ay = col + dy[di]
    while 0 <= ax < n and 0 <= ay < m:
        if cctv[ax][ay] == 0:
            cctv[ax][ay] = i
        elif cctv[ax][ay] == 6:
            return
        ax += dx[di]
        ay += dy[di]
    return


def erase(i, di, row, col):
    # while er:
    #     cctv[er[0][0]][er[0][1]] = 0
    #     del er[0]

    ax = row + dx[di]
    ay = col + dy[di]
    while 0 <= ax < n and 0 <= ay < m:
        if cctv[ax][ay] == i:
            cctv[ax][ay] = 0
        elif cctv[ax][ay] == 6:
            return
        ax += dx[di]
        ay += dy[di]
    return


def dfs(idx):
    global min_result
    if idx == len(arr):
        res = check()
        min_result = min(min_result, res)
        return

    a = cctv[arr[idx][0]][arr[idx][1]]
    for i in dir[a]:
        for j in i:
            visible(idx+7, j, arr[idx][0], arr[idx][1])
        dfs(idx+1)
        for j in i:
            erase(idx+7, j, arr[idx][0], arr[idx][1])

dfs(0)
print(min_result)