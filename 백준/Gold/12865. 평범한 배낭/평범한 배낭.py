N, M = map(int, input().split())
bag = [(0, 0)]
for _ in range(N):
    bag.append(tuple(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        w, v = bag[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][M])



