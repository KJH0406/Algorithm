def check(li):
    li2 = []
    for i in range(len(li)):
        temp = []
        for j in range(len(li)):
            temp.append(li[j][i])
        li2.append(temp)


    cnt = []
    for i in range(len(li)):
        count = 1
        for j in range(len(li)-1):
            if li[i][j] == li[i][j+1]:
                count += 1
            else:
                cnt.append(count)
                count = 1
        cnt.append(count)
    for i in range(len(li2)):
        count = 1
        for j in range(len(li2)-1):
            if li2[i][j] == li2[i][j+1]:
                count += 1
            else:
                cnt.append(count)
                count = 1
        cnt.append(count)
    return max(cnt)


N = int(input())
candy = [list(input()) for _ in range(N)]
candy2 = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(candy[j][i])
    candy2.append(temp)
res = []
for i in range(N):
    for j in range(N-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            res.append(check(candy))
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j + 1]

for i in range(N):
    for j in range(N-1):
        if candy2[i][j] != candy2[i][j+1]:
            candy2[i][j], candy2[i][j+1] = candy2[i][j+1], candy2[i][j]
            res.append(check(candy2))
            candy2[i][j + 1], candy2[i][j] = candy2[i][j], candy2[i][j + 1]

print(max(res))


