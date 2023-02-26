T = int(input())
arr = [[0] * 100 for _ in range(100)]
count = 0

for _ in range(T):
    x, y = map(int, input().split())
    for si in range(y, y+10):
        for sj in range(x, x+10):
            arr[si][sj] += 1
            
for i in range(100):
    for j in range(100):
        if arr[i][j] > 0:
            count += 1
print(count)

