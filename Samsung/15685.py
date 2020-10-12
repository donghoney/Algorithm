n = int(input())
inform = [list(map(int, input().split())) for _ in range(n)]
dragon_map = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
cx = [0, 1, 1]
cy = [1, 1, 0]
ans = 0

def make_curve(di, gen):
    res = [[0, 0], [dx[di], dy[di], di]]

    for i in range(gen):
        for j in range(len(res)-1, 0, -1):
            di = (res[j][2] + 1) % 4
            res.append([res[-1][0]+dx[di], res[-1][1]+dy[di], di])

    return res

for i in inform:
    tmp = make_curve(i[2], i[3])
    for t in tmp:
        ax = i[1] + t[0]
        ay = i[0] + t[1]
        if 0 <= ax < 101 and 0 <= ay < 101:
            dragon_map[ax][ay] = 1

for i in range(101):
    for j in range(101):
        if dragon_map[i][j] == 1:
            cnt = 0
            for k in range(3):
                tx = i + cx[k]
                ty = j + cy[k]
                if 0 <= tx < 101 and 0 <= ty < 101:
                    if dragon_map[tx][ty] == 1:
                        cnt += 1
            if cnt == 3:
                ans += 1

print(ans)