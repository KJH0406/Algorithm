N = int(input())
res = []
for _ in range(N):
    temp = list(input().split())
    res.append(temp)
res.sort(reverse=True)
res.sort(key=lambda x: x[0])
for item in res:
    print(*item)