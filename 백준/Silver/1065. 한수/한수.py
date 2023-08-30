n = int(input())

res = 0
for i in range(1, n + 1):
    ans = str(i)
    temp = list(map(int, ans))
    if i < 100:
        res += 1
    elif temp[0] - temp[1] == temp[1] - temp[2]:
        res += 1
print(res)