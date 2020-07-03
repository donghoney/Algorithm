li = []
ch = []

for i in range(10):
    a = int(input())
    li.append(a%42)

for i in range(10):
    if li[i] not in ch:
        ch.append(li[i])

print(len(ch))