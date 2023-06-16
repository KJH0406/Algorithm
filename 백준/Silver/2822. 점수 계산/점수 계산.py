nums = [0] + [int(input()) for _ in range(8)]
idx = []
s = 0

for i in range(1, 9):
    cnt = 0
    for item in nums:
        if nums[i] > item:
            cnt += 1
    if cnt > 3:
        idx.append(i)
        s += nums[i]
print(s)
print(*idx)
