n = int(input())
nums = list(map(int, input().split()))
nums.sort()
temp = []

for i in range(n):
    s = 0
    for j in range(n):
        s += abs(nums[i] - nums[j])
    temp.append(s)

minV = min(temp)
for i in range(n):
    if temp[i] == minV:
        print(nums[i])
        break

