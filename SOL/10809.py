name = input()
for i in range(97,123):
    if chr(i) in name:
        print(name.find(chr(i)), end=' ')
    else:
        print('-1', end=' ')