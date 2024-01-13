n = int(input())  # 기간
profit = [0] * (n + 1)  # 기간 내 얻을 수 있는 수익

for i in range(1, n + 1):
    t, p = map(int, input().split())  # t : 상담을 완료 하는데 걸리는 시간, p : 상담을 했을 때 받을 수 있는 금액

    # 해당 날짜에 상담 진행 가능한 경우
    if i + t <= n + 1:
        profit[i] += p
    # 상담에 필요한 기간 이후 에는 상담을 진행 할 수 있음
    for j in range(i + t, n + 1):
        profit[j] = max(profit[j], profit[i])

print(max(profit))  # 최대 수익 출력