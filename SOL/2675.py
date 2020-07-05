num = int(input())
li = []
for i in range(num):
    tmp = ''
    a, b = input().split()
    for j in b:
        tmp += j*int(a)
    li.append(tmp)

for i in li:
    print(i)