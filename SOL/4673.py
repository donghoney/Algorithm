def d(a):
    a = a + sum([int(i) for i in str(a)])
    return a

self_num = []
for i in range(1, 10001):
    if i not in self_num:
        print(i)
    self_num.append(d(i))