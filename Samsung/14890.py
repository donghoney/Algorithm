N, L = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(N)]
column = [[0]*N for _ in range(N)]
ans = 0


def check(li):
    global ans
    board = [0]*N
    if li.count(li[0]) == N:
        ans += 1
        return

    for i in range(1, N):

        if abs(li[i-1] - li[i]) >= 2: # 높이 차이 2이상 나면 볼것 x
            return

        if li[i-1] == li[i]:
            pass

        if li[i-1] - li[i] == 1:  # 앞에가 1 더 클 때
            if i+L > N or board[i] > 0:      # 범위 벗어나면
                return
            else:            # 놓을 수 있을 때
                for j in range(i, i+L):
                    board[j] = 1

        elif li[i-1] - li[i] == -1:
            if i-L < 0:      # 범위 벗어나면
                return
            else:            # 놓을 수 있을 때
                for j in range(i-L, i):
                    if board[j] == 1:
                        return
                    board[j] = 1

    ans += 1
    return


for i in range(N):
    for j in range(N):
        column[j][i] = load[i][j]

for i in range(N):
    check(load[i])
    check(column[i])

print(ans)