def star(a):
    s = '*'
    space = ' '
    tmp1 = ''
    tmp2 = ''

    for i in range(a):
        if i%2 == 0:
            tmp1 += s
            tmp2 += space
        else:
            tmp1 += space
            tmp2 += s
    print(tmp1)
    print(tmp2)


num = int(input())

for i in range(num):
    star(num)