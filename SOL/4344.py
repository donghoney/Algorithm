num = int(input())
result = []

for i in range(num):
    sum = 0
    k = 0
    li = list(map(int, input().split()))
    for j in range(1,len(li)):
        sum += li[j]
    avg = sum / li[0]
    for j in range(1, len(li)):
        if li[j] > avg:
            k += 1
    result.append((k/li[0])*100)

for i in range(num):
    print("{0:.3f}%".format(result[i]))