weight = int(input())

five = int(weight / 5)

for i in reversed(range(five+1)):
    remain = weight - (i*5)
    if remain == 0:
        print(i)
        break
    elif remain % 3 == 0:
        print(i+int(remain/3))
        break
    elif i==0 and remain%3 != 0:
        print('-1')
        break
