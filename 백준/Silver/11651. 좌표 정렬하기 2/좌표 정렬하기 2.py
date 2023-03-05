N = int(input())
res = []
p = []
for _ in range(N):
    x, y = map(int, input().split())
    res.append((x, y))
res.sort(key=lambda x:(x[1], x[0]))
for item in res:
    print(*item)