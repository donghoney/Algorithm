import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i]==0 and matrix[v][i]==1:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())
matrix = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

cnt = 0
for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        cnt+=1
print(cnt)