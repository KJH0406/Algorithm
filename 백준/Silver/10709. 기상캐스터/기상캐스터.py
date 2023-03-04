H, W = map(int, input().split())
for _ in range(H):
    cloud = list(input())
    res = []
    for i in range(W):
        if cloud.count('c') == 0:
            for _ in range(W):
                res.append(-1)
            break
        else:
            if cloud[i] == '.' and i == 0:
                res.append(-1)
            elif cloud[i] == 'c':
                res.append(0)
            else:
                cnt = 0
                count = 0
                while True:
                    if cloud[i] == 'c':
                        res.append(count)
                        cnt += 1
                        break
                    elif i == 0:
                        break
                    else:
                        count += 1
                        i -= 1
                if cnt == 0:
                    res.append(-1)
    print(*res)
