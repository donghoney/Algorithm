from collections import deque

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            cleaner.append([i, j])


def spread():
    sp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                spare = room[i][j] // 5
                for k in range(4):
                    ai = i + dx[k]
                    aj = j + dy[k]
                    if 0 <= ai < r and 0 <= aj < c and room[ai][aj] != -1:
                        sp[ai][aj] += spare
                        room[i][j] -= spare

    for i in range(r):
        for j in range(c):
            room[i][j] += sp[i][j]


def move(x, y, ud):
    q = deque()
    di = 1
    ax = x + dx[di]
    ay = y + dy[di]
    while room[ax][ay] != -1:
        tmp = 0
        if q:
            tmp = q.popleft()
        if room[ax][ay] > 0:
            q.append(room[ax][ay])
        room[ax][ay] = tmp

        if 0 <= (ax + dx[di]) < r and 0 <= (ay + dy[di]) < c:
            pass
        elif ud == 0:
            di -= 1
        elif ud == 1:
            di = (di + 1) % 4
        ax += dx[di]
        ay += dy[di]

for i in range(t):
    spread()
    move(cleaner[0][0], cleaner[0][1], 0)
    move(cleaner[1][0], cleaner[1][1], 1)

ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            ans += room[i][j]

print(ans)