import sys

N, K = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

# 첫번째 부분 리스트의 합을 계산합니다.
sum_ = sum(temperature[:K])

res = [sum_]

for i in range(K, N):
    # 이전 결과에서 첫 번째 원소를 빼고, K+1번째 원소를 더합니다.
    sum_ = sum_ - temperature[i-K] + temperature[i]
    res.append(sum_)

print(max(res))