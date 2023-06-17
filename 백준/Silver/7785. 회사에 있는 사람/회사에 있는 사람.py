n = int(input())
res = []
for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        res.append(a)
    elif b == 'leave':
        res.remove(a)
res.sort(reverse=True)
for item in res:
    print(item)