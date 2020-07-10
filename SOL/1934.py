def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)

num = int(input())
xlist= []
ylist = []

for i in range(num):
    a, b = map(int, input().split())
    xlist.append(a)
    ylist.append(b)

for i in range(num):
    print(lcm(xlist[i],ylist[i]))