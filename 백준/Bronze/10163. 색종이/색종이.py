arr = [[0]*1001 for _ in range(1001)]
N = int(input())
for i in range(1, N + 1):
    x, y, wide, height = map(int, input().split())
    for sj in range(wide):
        for si in range(height):
            arr[si+y][sj+x] = i

for i in range(1, N+1):
    count = 0
    for k in range(1001):
        for j in range(1001):
            if arr[k][j] == i:
                count += 1
    print(count)
