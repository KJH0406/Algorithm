n = int(input())
nums = list(map(int, input().split()))
nums.sort()
s = 0
total_sum = sum(nums)  # 누적합을 위한 전체 덧셈 계산
for i in range(n):  # nums에서 원소 호출
    total_sum -= nums[i]  # 전체 합에서 해당 값 제외
    s += nums[i] * total_sum  # 누적합에 전체 합과 해당 값을 곱한 값을 더해줌.

print(s)