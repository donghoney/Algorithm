from collections import deque
import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
block = [[0]*n for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
q = deque()

q.append((board, 0))

def move(di, maps):
    visit = [[0] * n for _ in range(n)]
    if di // 2 == 0:
        start = 0
        fin = n
        rev = 1
    else:
        start = n-1
        fin = -1
        rev = -1

    for i in range(start, fin, rev):
        for j in range(start, fin, rev):
            if maps[i][j] != 0:
                ax = i + dx[di]
                ay = j + dy[di]
                while 0 <= ax < n and 0 <= ay < n:
                    if maps[ax-dx[di]][ay-dy[di]] == maps[ax][ay] and visit[ax][ay] == 0:
                        maps[ax][ay] += maps[ax-dx[di]][ay-dy[di]]
                        maps[ax-dx[di]][ay-dy[di]] = 0
                        visit[ax][ay] = 1
                        break
                    elif maps[ax][ay] != 0 and maps[i][j] != maps[ax][ay]:
                        break
                    else:
                        maps[ax][ay] = maps[ax-dx[di]][ay-dy[di]]
                        maps[ax - dx[di]][ay - dy[di]] = 0
                        ax = ax + dx[di]
                        ay = ay + dy[di]
    return maps

def bfs():
    max_block = 0
    while q:
        block_list, depth = q.popleft()
        m = 0
        for i in range(n):
            m = max(m, max(block_list[i]))
        max_block = max(max_block, m)

        if depth > 5:
            break
        for k in range(4):
            copy_block = copy.deepcopy(block_list)
            tmp = move(k, copy_block)
            q.append((tmp, depth+1))
    print(max_block)

bfs()