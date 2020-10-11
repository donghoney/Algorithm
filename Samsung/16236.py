from collections import deque


def move(x, y):
    visit = [[0]*n for _ in range(n)]
    t = [[0]*n for _ in range(n)]
    eat = []
    visit[x][y] = 1
    queue = deque()
    queue.append([x, y])

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            ax = cur_x + dx[i]
            ay = cur_y + dy[i]
            if 0 <= ax < n and 0 <= ay < n and visit[ax][ay] == 0:
                if space[ax][ay] == 0 or space[ax][ay] <= space[x][y]:
                    queue.append([ax, ay])
                    visit[ax][ay] = 1
                    t[ax][ay] = t[cur_x][cur_y] + 1
                if 0 < space[ax][ay] < space[x][y]:
                    eat.append([ax, ay, t[ax][ay]])

    if not eat:
        return -1, -1, -1
    eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0
while True:
    nx, ny, t = move(start[0], start[1])
    if nx == -1: break
    space[nx][ny] = space[start[0]][start[1]]
    space[start[0]][start[1]] = 0
    start = [nx, ny]
    exp += 1
    if exp == space[nx][ny]:
        space[nx][ny] += 1
        exp = 0
    cnt += t
print(cnt)