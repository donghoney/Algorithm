from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visit[rx][ry][bx][by] = 1

def move(x, y, dir_x, dir_y):
    cnt = 0
    while board[x + dir_x][y + dir_y] != "#" and board[x][y] != "O":
        x += dir_x
        y += dir_y
        cnt += 1
    return x, y, cnt

def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            new_rx, new_ry, cnt_r = move(rx, ry, dx[i], dy[i])
            new_bx, new_by, cnt_b = move(bx, by, dx[i], dy[i])

            if board[new_bx][new_by] == "O":
                continue
            if board[new_rx][new_ry] == "O":
                print(depth)
                return

            if new_rx == new_bx and new_ry == new_by:
                if cnt_r > cnt_b:
                    new_rx -= dx[i]
                    new_ry -= dy[i]
                else:
                    new_bx -= dx[i]
                    new_by -= dy[i]

            if visit[new_rx][new_ry][new_bx][new_by] == 0:
                q.append((new_rx, new_ry, new_bx, new_by, depth+1))
                visit[new_rx][new_ry][new_bx][new_by] = 1
    print(-1)

bfs()