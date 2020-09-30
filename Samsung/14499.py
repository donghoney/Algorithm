row, col, start_x, start_y, num = map(int, input().split())

dice_map = [list(map(int, input().split())) for _ in range(row)]
move_list = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
answer = []

index = 0
up = 1
right = 2


def map_over(x, y, i):
    global row, col
    if i == 1:
        if col == y + 1:
            return False
    elif i == 2:
        if y - 1 < 0:
            return False
    elif i == 3:
        if x - 1 < 0:
            return False
    elif i == 4:
        if row == x + 1:
            return False
    return True


def move(i):
    global index, up, right
    if i == 1:
        tmp = 5 - index
        index = right
        right = tmp
    elif i == 2:
        tmp = index
        index = 5 - right
        right = tmp
    elif i == 3:
        tmp = 5 - index
        index = up
        up = tmp
    elif i == 4:
        tmp = index
        index = 5 - up
        up = tmp


for i in move_list:
    if map_over(start_x, start_y, i):
        move(i)
        if i == 1:
            start_y += 1
        elif i == 2:
            start_y -= 1
        elif i == 3:
            start_x -= 1
        elif i == 4:
            start_x += 1

        if dice_map[start_x][start_y] == 0:
            dice_map[start_x][start_y] = dice[index]
        else:
            dice[index] = dice_map[start_x][start_y]
            dice_map[start_x][start_y] = 0
        answer.append(dice[5-index])

for i in answer:
    print(i)