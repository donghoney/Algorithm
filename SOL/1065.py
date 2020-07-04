def hansu(a):
    cnt = 99
    for i in range(100, int(a)+1):
        i = str(i)
        if int(i) < 1000:
            if int(i[2])-int(i[1]) == int(i[1])-int(i[0]):
                cnt += 1
        else:
            if int(i[3])-int(i[2]) == int(i[2])-int(i[1]) == int(i[1])-int(i[0]):
                cnt += 1
    return cnt

num = input()

if len(num) < 3:
    print(int(num))
else:
    print(hansu(num))
