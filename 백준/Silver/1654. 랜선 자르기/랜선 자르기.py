K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]

left = 1
right = max(line)
res = []

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for item in line:
        cnt += item // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)
