n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

# 3부터 시작
for i in range(3, n+1):
    res = dp[i - 1] + dp[i - 2]
    # 15746으로 나눠야함
    dp[i] = res % 15746

#결과 출력
print(dp[n])