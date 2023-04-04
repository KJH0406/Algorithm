K, N = map(int, input().split())
line = list(map(int, input().split()))

left = 1
right = max(line)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for item in line:
        if item - mid > 0:
            cnt += item - mid
    if cnt > N:
        left = mid + 1
    elif cnt < N:
        right = mid - 1
    else:
        left = mid + 1

print(left-1)

