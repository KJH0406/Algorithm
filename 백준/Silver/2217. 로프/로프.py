N = int(input())
k = []

for _ in range(N):
    k.append(int(input()))
k.sort()
res = []
for i in k:
    res.append(i * N)
    N -= 1
print(max(res))