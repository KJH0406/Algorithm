x = int(input())
m = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for i in range(len(m)):
    if x >= m[i]:
        cnt += 1
        x -= m[i]
    if x == 0:
        break
print(cnt)