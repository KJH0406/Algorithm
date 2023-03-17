N, M, K = map(int, input().split())
arr = [['.'] * (M+2) for _ in range(N + 2)]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = '#'

food = []
queue = []
visited = [[False] * (M+2) for _ in range(N+2)]
si = sj = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == '#':
            si, sj = i, j
            queue.append((si, sj))
            visited[si][sj] = True
            cnt = 1
            while queue:
                ci, cj = queue.pop()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = ci + di, cj + dj
                    if arr[ni][nj] == '#' and not visited[ni][nj]:
                        queue.append((ni, nj))
                        visited[ni][nj] = True
                        cnt += 1
            food.append(cnt)
print(max(food))