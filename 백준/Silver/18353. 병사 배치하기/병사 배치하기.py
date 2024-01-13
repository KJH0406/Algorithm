n = int(input())

soldier = list(map(int, input().split()))

soldier = soldier[:: -1]

dp = [1] * n

for i in range(n):
    for j in range(i):
        if soldier[i] > soldier[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(n - max(dp))