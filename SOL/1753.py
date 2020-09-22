import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
inf = sys.maxsize

arr = [inf] * (V+1)
dis = [[] for _ in range(V+1)]
heap = []


def dijk(start):
    arr[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        weight, node = heapq.heappop(heap)

        for n, wei in dis[node]:
            next_w = wei + weight
            if next_w < arr[n]:
                arr[n] = next_w
                heapq.heappush(heap, [next_w, n])


for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    dis[u].append([v, w])

dijk(k)
for i in arr[1:]:
    print(i if i != inf else "INF")