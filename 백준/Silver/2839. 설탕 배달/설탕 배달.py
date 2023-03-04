N = int(input())
five = N
cnt = 0
res = []
while five > 4:
    cnt += 1
    five -= 5

for i in range(cnt+1):
    if (N - 5 * i) % 3 == 0:
        res.append(((N - 5 * i) // 3, i))
res.sort()
if res:
    print(res[0][0] + res[0][1])
else:
    print(-1)