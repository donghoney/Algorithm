def sol(n, arr, m, s):

    for i in range(len(arr)):
        tmp = arr[i] - m
        if tmp > 0 and tmp % s == 0:
            n += (tmp/s)
        elif tmp > 0 and tmp % s != 0:
            n += (tmp//s)+1

    return int(n)


N = int(input())
arr = list(map(int, input().split()))
master, sub = map(int, input().split())
print(sol(N, arr, master, sub))