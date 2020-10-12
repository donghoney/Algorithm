def solution(triangle):
    dp = []

    for i in range(len(triangle)):
        dp.append([0])
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][0] = (dp[i - 1][j] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                dp[i].append(dp[i - 1][j - 1] + triangle[i][j])
            else:
                max_res = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])
                dp[i].append(max_res)

    answer = max(dp[-1])
    return answer

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
print(solution(triangle))