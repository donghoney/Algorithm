num = int(input())
star = ''

for i in range(1, 2*num):
    if i <= num:
        star = star + '*'
        print(star)
    else:
        tmp = i - num
        print(star[:num-tmp])