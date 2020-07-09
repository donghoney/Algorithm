input = int(input())

it = 1
num = 0
while True:
    num += it
    if input <= num:
        if it%2 == 0:
            print('{}/{}'.format((it-(num-input)),(num-input+1)))
            break
        else:
            print('{}/{}'.format((num - input + 1), (it - num + input)))
            break
    it+=1