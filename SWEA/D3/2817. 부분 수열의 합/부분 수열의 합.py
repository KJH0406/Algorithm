def dfs(n, sm, cnt):
    global ans

    if sm == K:
        ans += 1
        return

    for j in range(cnt, N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm + arr[j], j)
            v[j] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    v = [0] * N
    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')

