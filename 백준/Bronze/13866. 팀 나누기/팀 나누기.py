nums = list(map(int, input().split()))
nums.sort()
print(abs(nums[0] + nums[-1] - nums[1] - nums[2]))