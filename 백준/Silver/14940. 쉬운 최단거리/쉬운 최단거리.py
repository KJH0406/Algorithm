from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue = deque()

ci = cj = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            ci, cj = i, j
            queue.append((i, j))
            break

cnt = 1
visited[ci][cj] = cnt

while queue:
    si, sj = queue.popleft()
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
            queue.append((ni, nj))
            visited[ni][nj] = visited[si][sj] + 1
        elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1

for i in range(N):
    temp = deque()
    for j in range(M):
        if arr[i][j] == 0:
           temp.append(0)
        else:
            temp.append(visited[i][j] - 1)
    print(*temp)

