def group(a):
    li = []
    for i in range(len(a)):
        if i == 0:
            li.append(a[i])
        elif a[i] == a[i-1]:
            pass
        elif a[i] not in li:
            li.append(a[i])
        elif a[i] in li:
            return 0
    return 1

num = int(input())
cnt = 0
for i in range(num):
    word = input()
    cnt += group(word)
print(cnt)