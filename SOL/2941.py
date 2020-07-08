alphabet = input()
cnt = 0

for i in range(len(alphabet)):
    if alphabet[i] == '=':
        if i>=1 and alphabet[i-1] in ['c', 'z', 's']:
            if i>=2 and alphabet[i-1] == 'z' and alphabet[i-2] == 'd':
                cnt -= 1
            else:
                pass
    elif alphabet[i] == '-':
        if i>=1 and alphabet[i-1] in ['c', 'd']:
            pass
    elif alphabet[i] == 'j':
        if i>=1 and alphabet[i-1] in ['l', 'n']:
            pass
        else:
            cnt+=1
    else:
        cnt+=1
print(cnt)