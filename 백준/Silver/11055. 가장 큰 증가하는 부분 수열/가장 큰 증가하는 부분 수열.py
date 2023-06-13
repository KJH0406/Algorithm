N = int(input())

numbers = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
    dp_max = 0
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            dp_max = max(dp_max, dp[j])
    dp[i] = dp_max + numbers[i]

print(max(dp))


