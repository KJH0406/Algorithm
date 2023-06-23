N = int(input())
cups = [int(input()) for _ in range(N)]
if N <= 2:
    print(sum(cups))
else:
    res = 0
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = [cups[0], cups[0], 0]
    dp[1] = [cups[0] + cups[1], cups[1], cups[0]]
    for i in range(2, N):
        dp[i] = [dp[i-1][1] + cups[i], max(dp[i-2]) + cups[i], max(dp[i-1])]
        if res < max(dp[i]):
            res = max(dp[i])
    print(res)
