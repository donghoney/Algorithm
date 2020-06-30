a = input()
cycle = 0

def make_two(a):
    a = '0' + a
    return a

if len(a) == 1:
    a = make_two(a)

org_a = a
while True:
    tmp = int(a[0]) + int(a[1])
    tmp = str(tmp)
    if len(tmp) == 1:
        tmp = make_two(tmp)
    a = a[1] + tmp[1]
    cycle += 1

    if a == org_a:
        print(cycle)
        break

