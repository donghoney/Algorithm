num = int(input())
li=list(map(int,input().split()))

if len(li) == num:
    print(min(li), max(li))