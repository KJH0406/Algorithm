import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] + [k+1] * k
coin = [int(input()) for _ in range(n)]

for c in coin:
    for j in range(1, k+1):
        if j-c >= 0:
            dp[j] = min(dp[j], dp[j-c]+1)

if dp[k] != k+1:
    print(dp[k])
else:
    print(-1)

