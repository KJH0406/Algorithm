n = int(input())
nums = [float(input()) for _ in range(n)]
nums.sort()
for i in range(7):
    print(f'{nums[i]:.3f}')



