num = int(input())
li = list(map(int,input().split()))

for i in range(num-1,-1,-1):
    if i == 0:
        print('-1')
        break
    if li[i-1] < li[i]:
        upper_min = max(li)
        min_idx = li.index(upper_min)
        for j in range(i,num):
            if li[j] > li[i-1] and li[j] < upper_min:
                upper_min = li[j]
                min_idx = j
        li[min_idx] = li[i-1]
        li[i-1] = upper_min
        li = li[:i] + sorted(li[i:])
        for i in li:
            print(i, end=' ')
        break