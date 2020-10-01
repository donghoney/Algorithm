dic = {}
for i in range(1,5):
    dic[i] = input()

rotate_num = int(input())
idx = [0, 0, 0, 0]


def rotate_R(num, dir):
    tmp = idx[num-1]
    if num <= 4:
        if dir == -1:
            idx[num-1] = (idx[num-1] + 1) % 8

        elif dir == 1:
            if idx[num-1] == 0:
                idx[num-1] = 7
            else: idx[num-1] = idx[num-1] - 1

        if num < 4 and dic[num][(tmp+2)%8] != dic[num+1][(idx[num]+6)%8]:
            rotate_R(num+1, -dir)
        return
    return


def rotate_L(num, dir, i, ch):
    if num >= 1:
        if dir == -1:
            if ch == 1:
                idx[num-1] = (idx[num-1] + 1) % 8
        else:
            if ch == 1:
                if idx[num-1] == 0:
                    idx[num-1] = 7
                else:
                    idx[num-1] = idx[num-1] - 1

        if num > 1 and dic[num][(i+6)%8] != dic[num-1][(idx[num-2]+2)%8]:
            rotate_L(num - 1, -dir, idx[num - 2], 1)
        return
    return


for i in range(rotate_num):
    num, dir = map(int, input().split())
    tmp = idx[num-1]
    if num == 1:
        rotate_R(num, dir)
    elif num == 4:
        rotate_L(num, dir, tmp, 1)
    else:
        rotate_R(num, dir)
        rotate_L(num, dir, tmp, 0)

count = 0
if dic[1][idx[0]] == '1':
    count += 1
if dic[2][idx[1]] == '1':
    count += 2
if dic[3][idx[2]] == '1':
    count += 4
if dic[4][idx[3]] == '1':
    count += 8

print(count)