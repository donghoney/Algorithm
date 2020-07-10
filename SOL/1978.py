n = 1000
a = [False, False] + [True]*(n-1)
prime = []

for i in range(n):
    if a[i]:
        prime.append(i)
        for j in range(2*i,n+1,i):
            a[j] = False

num = int(input())
sum = 0
li = list(map(int, input().split()))
for i in range(num):
    if li[i] in prime:
        sum += 1
print(sum)
