num = int(input())
li=list(map(int,input().split()))
avg = 0

if len(li) == num:
    m = max(li)
    for i in range(num):
        avg += (li[i]/m)*100
    print(avg/num)