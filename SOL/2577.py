a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)

li = [0 for i in range(10)]

for i in range(len(num)):
    li[int(num[i])] += 1

for i in range(len(li)):
    print(li[i])