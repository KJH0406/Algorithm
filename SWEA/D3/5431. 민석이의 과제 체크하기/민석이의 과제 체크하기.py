T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    problem = list(map(int, input().split()))
    res = []
    c = 1
    for i in range(1, N+1):
        res.append(c)
        c += 1

    for num in problem:
        if num in res:
            res.remove(num)
    print(f'#{tc}', *res)




