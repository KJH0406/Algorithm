import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [1] + [0] * k
coin = [int(input()) for _ in range(n)]

for c in coin:
    for j in range(c, k+1):
        dp[j] = dp[j] + dp[j-c]

print(dp[k])
