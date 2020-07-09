a, b, v = map(int, input().split())

if (v-a)/(a-b) > int((v-a)/(a-b)):
    tmp = int((v-a)/(a-b))+1
else:
    tmp = int((v-a)/(a-b))

print(tmp+1)