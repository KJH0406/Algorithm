from collections import deque

N, K = map(int, input().split())
dp = [0] * 100001
queue = deque()
cnt = 0
if N == K:
    print(0)
else:
    queue.append(N)
    dp[N] = 1
    while queue:
        cp = queue.popleft()
        if cp == K:
            break
        back = cp - 1
        go = cp + 1
        tp = cp * 2
        if 0 <= back <= 100000 and dp[back] == 0:
            dp[back] = dp[cp] + 1
            queue.append(back)
        if 0 <= tp <= 100000 and dp[tp] == 0:
            queue.append(tp)
            dp[tp] = dp[cp]
        if 0 <= go <= 100000 and dp[go] == 0:
            dp[go] = dp[cp] + 1
            queue.append(go)
    print(dp[K]-1)
