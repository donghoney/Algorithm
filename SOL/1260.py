n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def dfs(node):
    print(node, end=' ')
    visit[node] = 1
    for i in range(1, n+1):
        if visit[i]==0 and matrix[node][i]==1:
            dfs(i)

def bfs(node):
    queue = [node]
    visit[node] = 0
    while queue:
        num = queue[0]
        print(num, end=' ')
        del queue[0]
        for i in range(1,n+1):
            if visit[i]==1 and matrix[num][i]==1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)