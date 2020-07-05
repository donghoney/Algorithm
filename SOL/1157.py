sen = input().lower()
dic = {}
for i in sen:
    if i not in dic:
        dic[i] = 0
    else:
        dic[i] += 1

dic_max = max(dic.values())

max_dup = 0
for v in dic.values():
    if v == dic_max:
        max_dup += 1

if max_dup >= 2:
    print('?')
else:
    key_max = max(dic.keys(), key=(lambda k:dic[k]))
    print(key_max.upper())
