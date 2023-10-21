N, M = map(int, input().split())
nums = list(map(int, input().split()))
l, r = 0, 1
res = 0
while r <= N and l <= r:
    S = nums[l:r]
    T = sum(S)
    if T == M:
        res += 1
        r += 1
    elif T < M:
        r += 1
    else:
        l += 1

print(res)