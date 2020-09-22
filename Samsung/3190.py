# 뱀 문제
def move(index, map, dic):
    direct = ["R", "D", "L", "U"]
    snake = []
    time = 0
    x, y = 0, 0
    tx, ty = 0, 0
    map[x][y] = 2

    while True:
        time += 1
        if direct[index] == "R":
            y += 1
        elif direct[index] == "D":
            x += 1
        elif direct[index] == "L":
            y -= 1
        else:
            x -= 1

        if x >= len(map) or y >= len(map) or x < 0 or y < 0 or map[x][y] == 2:
            break

        if map[x][y] == 0:
            map[tx][ty] = 0
            snake.append([x, y])
            tx, ty = snake.pop(0)
        else:
            snake.append([x, y])
        map[x][y] = 2

        if time in dic:
            if dic[time] == "D":
                index += 1
                index %= 4
            else:
                index -= 1
                if index < 0:
                    index = 3
    return time

N = int(input())
apple_num = int(input())
snake_map = [[0]*N for _ in range(N)]

for i in range(apple_num):
    x, y = map(int, input().split())
    snake_map[x-1][y-1] = 1

move_num = int(input())
dic = {}
for i in range(move_num):
    t, d = input().split()
    dic[int(t)] = d

print(move(0, snake_map, dic))