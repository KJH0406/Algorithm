from collections import deque

N, K = map(int, input().split())
dp = [[987654321, 0] for _ in range(100001)]
queue = deque()
if N == K:
    print(0)
    print(1)
else:
    queue.append(N)
    dp[N][0] = 1
    dp[N][1] = 1
    while queue:
        cp = queue.popleft()
        back = cp - 1
        go = cp + 1
        tp = cp * 2
        if 0 <= tp <= 100000 and dp[tp][0] >= dp[cp][0] + 1:
            dp[tp][0] = dp[cp][0] + 1
            dp[tp][1] = dp[tp][1] + 1
            queue.append(tp)
        if 0 <= back <= 100000 and dp[back][0] >= dp[cp][0] + 1:
            queue.append(back)
            dp[back][0] = dp[cp][0] + 1
            dp[back][1] = dp[back][1] + 1
        if 0 <= go <= 100000 and dp[go][0] >= dp[cp][0] + 1:
            dp[go][0] = dp[cp][0] + 1
            dp[go][1] = dp[go][1] + 1
            queue.append(go)

    print(dp[K][0]-1)
    print(dp[K][1])



    