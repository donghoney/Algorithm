def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def gcdsum(arr):
    num = len(arr)-1
    sum = 0
    for i in range(num):
        for j in range(i+1, len(arr)):
            sum += gcd(arr[i], arr[j])
    return sum

num = int(input())
result = []

for i in range(num):
    li = list(map(int, input().split()))
    del li[0]
    result.append(gcdsum(li))

for i in result:
    print(i)