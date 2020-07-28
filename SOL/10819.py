from itertools import permutations

n = int(input())
arr = permutations(list(map(int, input().split())))
ans = 0
for a in arr:
    sums = 0
    for i in range(n-1):
        sums+=abs(a[i]-a[i+1])
    ans = max(ans, sums)
print(ans)