def dfs(n, lst):
    if n == M:
        return ans.append(lst)

    prev = 0
    for j in range(N):
        if visited[j] == 0 and prev != M_list[j]:
            prev = M_list[j]
            visited[j] = 1
            dfs(n+1, lst + [M_list[j]])
            visited[j] = 0


N, M = map(int, input().split())
M_list = sorted(list(map(int, input().split())))
ans = []
visited = [0] * N

dfs(0, [])
for lst in ans:
    print(*lst)
