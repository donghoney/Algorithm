r, c, m = map(int, input().split())
board = [[0]*c for _ in range(r)]

for _ in range(m):
    y, x, s, d, z = map(int, input().split())
    board[y-1][x-1] = (s, d-1, z)


def catch(column):
    size = 0
    for idx in range(r):
        if board[idx][column] != 0:
            speed, di, size = board[idx][column]
            board[idx][column] = 0
            break
    return size


def move():
    new_board = [[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] != 0:
                speed, i, size = board[y][x]

                if i == 0 or i == 1:
                    speed %= ((r-1)*2)
                elif i == 2 or i == 3:
                    speed %= ((c-1)*2)

                ny, nx = y, x
                if ny == 0 and i == 0:
                    i = 1
                elif ny == (r-1) and i == 1:
                    i = 0
                elif nx == 0 and i == 3:
                    i = 2
                elif nx == (c-1) and i == 2:
                    i = 3

                for _ in range(speed):
                    if i == 0:
                        ny -= 1
                        if ny - 1 < 0:
                            i = 1
                    elif i == 1:
                        ny += 1
                        if ny + 1 >= r:
                            i = 0
                    elif i == 2:
                        nx += 1
                        if nx + 1 >= c:
                            i = 3
                    elif i == 3:
                        nx -= 1
                        if nx - 1 < 0:
                            i = 2

                if new_board[ny][nx] == 0 or size > new_board[ny][nx][2]:
                    new_board[ny][nx] = (speed, i, size)
    return new_board


ans = 0
for i in range(c):
    ans += catch(i)
    board = move()

print(ans)