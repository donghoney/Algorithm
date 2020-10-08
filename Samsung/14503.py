n, m = map(int, input().split())
r, c, d = map(int, input().split())
clean = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0


def move(x, y, di):
    global ans
    queue = [[x, y]]

    while queue:
        cur = queue.pop()
        no = 0

        if clean[cur[0]][cur[1]] == 0:
            clean[cur[0]][cur[1]] = 2
            ans += 1

        for i in range(1, 5):
            ax = cur[0] + dx[di - i]
            ay = cur[1] + dy[di - i]
            if 0 <= ax < n and 0 <= ay < m and clean[ax][ay] == 0:
                queue.append([ax, ay])
                di = (di-i+4) % 4
                break
            else:
                no += 1

        if no == 4 and clean[cur[0]+dx[di-2]][cur[1]+dy[di-2]] == 1:
            break
        elif no == 4:
            queue.append([cur[0]+dx[di-2], cur[1]+dy[di-2]])

move(r, c, d)
print(ans)