year = 0
e,s,m = map(int,input().split())

while True:
    x,y,z = year%15,year%28,year%19

    if x==e-1 and y==s-1 and z==m-1:
        print(year+1)
        break
    year+=1