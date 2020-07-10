import sys
input = sys.stdin.readline

num_list = []

while True:
    n = int(input().strip())
    if n == 0:
        break
    num_list.append(n)

n = max(num_list)
a = [False, False] + [True]*(n-1)

for i in range(2,int(n**0.5)+1):
    if a[i]:
        for j in range(2*i,n+1,i):
            a[j] = False

prime = [i for i in range(n+1) if a[i] == True]

for x in num_list:
    for p in prime:
        if a[x-p]:
            print("%d = %d + %d" % (x, p, x - p))
            break