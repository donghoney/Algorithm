from collections import deque


def check(i, j):

    for k in range(4):
        ax = i + dx[k]
        ay = j + dy[k]
        if 0 <= ax < N and 0 <= ay < N and visit[ax][ay] == -1:
            if L <= abs(nat[i][j] - nat[ax][ay]) <= R:
                return True
    return False


N, L, R = map(int, input().split())
nat = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
q = deque([])

while True:
    visit = [[-1] * N for _ in range(N)]
    val_list = []
    num = 0

    for i in range(N):
        for j in range(N):

            if check(i, j):
                q.append([i, j])
                li = []

                while q:
                    x, y = q.popleft()

                    if visit[x][y] == -1:
                        visit[x][y] = num
                        li.append(nat[x][y])
                        for k in range(4):
                            ax = x + dx[k]
                            ay = y + dy[k]

                            if 0 <= ax < N and 0 <= ay < N and visit[ax][ay] == -1:
                                if [ax, ay] not in q and L <= abs(nat[x][y] - nat[ax][ay]) <= R:
                                    q.append([ax, ay])
                num += 1
                val_list.append(sum(li) // len(li))

    if num == 0:
        break


    for i in range(N):
        for j in range(N):
            if visit[i][j] >= 0:
                nat[i][j] = val_list[visit[i][j]]
    ans += 1

print(ans)