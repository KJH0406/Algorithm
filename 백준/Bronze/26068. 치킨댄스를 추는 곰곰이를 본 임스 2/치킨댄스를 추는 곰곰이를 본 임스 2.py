
N = int(input())
cnt = 0
for _ in range(N):
    temp = list(input())
    res = temp[2:]
    res = ''.join(res)
    if int(res) <= 90:
        cnt += 1
print(cnt)