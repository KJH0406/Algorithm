N = int(input())
n = N + 1
dp = [0] * n
dp[1] = 1
for i in range(2, n):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[N])