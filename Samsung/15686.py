from itertools import combinations

n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]
ch = []
ans = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 2:
            ch.append([i, j])


def cal(open):
    min_val = 10000
    cnt = 0
    for i in range(n):
        for j in range(n):
            if town[i][j] == 1:
                for o in open:
                    if (abs(i - o[0]) + abs(j - o[1])) < min_val:
                        min_val = abs(i - o[0]) + abs(j - o[1])
                cnt += min_val
                min_val = 10000
    ans.append(cnt)


num = [i for i in range(len(ch))]
com = list(combinations(num, m))
for c in com:
    tmp = []
    for k in c:
        tmp.append(ch[k])
    cal(tmp)

print(min(ans))