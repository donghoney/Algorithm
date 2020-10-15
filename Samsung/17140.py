r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

def check():
    try:
        if matrix[r-1][c-1] == k:
            return False
    except IndexError:
        return True
    return True

def cal_r():
    row_max = 0
    result = []

    for row in matrix:
        dic = {}
        tmp = []
        for i in row:
            if i not in dic and i != 0:
                dic[i] = 1
            elif i in dic and i != 0:
                dic[i] += 1
        sort_tuple = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        if len(sort_tuple) > 50:
            for t in range(50):
                tmp.append(sort_tuple[t][0])
                tmp.append(sort_tuple[t][1])
        else:
            for t in sort_tuple:
                tmp.append(t[0])
                tmp.append(t[1])
        row_max = max(row_max, len(tmp))
        result.append(tmp)

    for i in range(len(result)):
        while len(result[i]) != row_max:
            result[i].append(0)
    return result

def cal_c():
    col_max = 0
    result = []

    for col in range(len(matrix[0])):
        dic = {}
        tmp = []
        for row in range(len(matrix)):
            if matrix[row][col] not in dic and matrix[row][col] != 0:
                dic[matrix[row][col]] = 1
            elif matrix[row][col] in dic and matrix[row][col] != 0:
                dic[matrix[row][col]] += 1
        sort_tuple = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        if len(sort_tuple) > 50:
            for t in range(50):
                tmp.append(sort_tuple[t][0])
                tmp.append(sort_tuple[t][1])
        else:
            for t in sort_tuple:
                tmp.append(t[0])
                tmp.append(t[1])
        col_max = max(col_max, len(tmp))
        result.append(tmp)

    fin = [[0]*len(matrix[0]) for _ in range(col_max)]
    for i in range(len(result)):
        for j in range(len(result[i])):
            fin[j][i] = result[i][j]

    return fin

time = 0
while check() and time <= 100:
    row_len = len(matrix)
    col_len = len(matrix[0])
    if row_len >= col_len:
        matrix = cal_r()
    else:
        matrix = cal_c()

    time += 1

if time > 100:
    print(-1)
else:
    print(time)