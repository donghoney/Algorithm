score = []
score.append(int(input()))
score.append(int(input()))
score.append(int(input()))
score.append(int(input()))
score.append(int(input()))

for i in range(len(score)):
    if score[i] < 40:
        score[i] = 40

print(int(sum(score) / 5))