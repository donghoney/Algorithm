a, b, c = map(int, input().split())

if b < c:
    x = int(a / (c - b))
    print(x + 1)
else:
    print(-1)