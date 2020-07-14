li = []
for i in range(9):
    li.append(int(input()))

sum_high = sum(li)
key_b = 0

for i in range(0,8):
    for j in range(i+1,9):
        if li[i] != li[j] and sum_high-(li[i]+li[j])==100:
            a,b = li[i], li[j]
            li.remove(a)
            li.remove(b)
            li.sort()
            key_b = 1
            break
    if key_b==1:
        break

for i in li:
    print(i)