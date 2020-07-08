word = input()
num = 0

for i in word:
    if ord(i)==83 or ord(i)==86 or ord(i)>=89:
        num += int((ord(i) - 65) / 3) + 2
    else:
        num += int((ord(i) - 65)/3) + 3
print(num)