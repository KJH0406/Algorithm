def dfs(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return

    prev = 0
    for j in range(s, N):
        if v[j] == 0 and prev != lst[j]:
            v[j] = 1
            prev = lst[j]
            dfs(n+1, j, tlst + [lst[j]])
            v[j] = 0


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
v = [0] * N
ans = []
dfs(0, 0, [])

for lst in ans:
    print(*lst)