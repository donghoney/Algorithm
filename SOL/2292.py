num = int(input())
i = 1
cnt = 1

while True:
    if num <= i:
        print(cnt)
        break
    else:
        i += 6*cnt
        cnt+=1