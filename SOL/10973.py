num = int(input())
li = list(map(int,input().split()))

for i in range(num-1,-1,-1):
    if i == 0:
        print('-1')
        break
    if li[i-1] > li[i]:
        max = li[i]
        min_idx = i
        for j in range(i,num):
            if li[j] < li[i-1] and li[j] > max:
                max = li[j]
                min_idx = j
        li[min_idx] = li[i-1]
        li[i-1] = max
        li = li[:i] + sorted(li[i:], reverse=True)
        for i in li:
            print(i, end=' ')
        break