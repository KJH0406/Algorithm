n = int(input())
if n == 0:
    print(0)
else:
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    per = n * 15 / 100
    temp_per = 0
    per = str(per).split('.')
    if int(per[1][0]) >= 5:
        temp_per = int(per[0]) + 1
    else:
        temp_per = int(per[0])
    nums = nums[temp_per:n-temp_per]
    temp_res = 0
    res = sum(nums) / len(nums)
    res = str(res).split('.')
    if int(res[1][0]) >= 5:
        temp_res = int(res[0]) + 1
    else:
        temp_res = int(res[0])
    print(temp_res)
