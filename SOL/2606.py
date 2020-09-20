size = int(input())
conn = int(input())
virus = [[0] * (size+1) for _ in range(size+1)]

for i in range(conn):
    a, b = map(int, input().split())
    virus[a][b] = 1
    virus[b][a] = 1

    visit = []
    queue = [1]

    while queue:
        cur = queue.pop(0)
        visit.append(cur)

        for i in range(len(virus)):
            if virus[cur][i] and i not in visit and i not in queue:
                queue.append(i)

print(len(visit)-1)