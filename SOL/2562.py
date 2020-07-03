li = []
for i in range(9):
    li.append(int(input()))
    if i == 0:
        max = li[0]
        index = 1
    elif li[i]>max:
        max = li[i]
        index = i+1
print(max)
print(index)