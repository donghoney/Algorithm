from itertools import combinations

vowel = ['a','e','i','o','u']
leng, num = map(int,input().split())
alphabet = sorted(list(map(str,input().split())))

com = combinations(alphabet,leng)

for i in com:
    cnt = 0

    for j in i:
        if j in vowel:
            cnt+=1
    if cnt >= 1 and cnt <= leng-2:
        print(''.join(i))