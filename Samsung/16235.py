n, m, k = map(int, input().split())
A = [[5]*n for _ in range(n)]
addA = [list(map(int, input().split())) for _ in range(n)]
tree = [[{} for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    x, y, a = map(int, input().split())
    tree[x-1][y-1][a] = 1

def spring():

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tmp = {}
                die = 0
                for age in sorted(tree[i][j].keys()):
                    if age * tree[i][j][age] <= A[i][j]:
                        A[i][j] -= age * tree[i][j][age]
                        tmp[age+1] = tree[i][j][age]
                    else:
                        survive = A[i][j] // age
                        if not survive:
                            die += (age // 2) * tree[i][j][age]
                            continue
                        A[i][j] -= age * survive
                        tmp[age+1] = survive
                        die += (age // 2) * (tree[i][j][age] - survive)

                tree[i][j] = tmp
                A[i][j] += die


def fall():

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                num = 0
                for age in tree[i][j].keys():
                    if age % 5 == 0:
                        num += tree[i][j][age]
                if num:
                    for k in range(8):
                        ax = i + dx[k]
                        ay = j + dy[k]
                        if 0 <= ax < n and 0 <= ay < n:
                            if 1 not in tree[ax][ay].keys():
                                tree[ax][ay][1] = num
                            else:
                                tree[ax][ay][1] += num

def winter():
    for i in range(n):
        for j in range(n):
            A[i][j] += addA[i][j]


for _ in range(k):
    spring()
    fall()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += sum(tree[i][j].values())

print(ans)