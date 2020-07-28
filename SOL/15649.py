from itertools import permutations

n, leng = map(int, input().split())

li = []
for i in range(1,n+1):
    li.append(i)
li = permutations(li,leng)

for i in li:
    for j in i:
        print(j,end=' ')
    print()
print()