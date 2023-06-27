from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
point = [[], [], []]
point = deque(point)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            point[0].append((i, j))
        elif arr[i][j] == 'G':
            point[1].append((i, j))
        else:
            point[2].append((i, j))
cnt = 1
for k in range(3):
    for i, j in point[k]:
        if visited[i][j] == 0:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = cnt
            while queue:
                si, sj = queue.popleft()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[si][sj] == arr[ni][nj] and visited[ni][nj] == 0:
                        queue.append((ni, nj))
                        visited[ni][nj] = cnt
            cnt += 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
visited = [[0] * N for _ in range(N)]

cnt2 = 1
for k in range(3):
    for i, j in point[k]:
        if visited[i][j] == 0:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = cnt2
            while queue:
                si, sj = queue.popleft()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[si][sj] == arr[ni][nj] and visited[ni][nj] == 0:
                        queue.append((ni, nj))
                        visited[ni][nj] = cnt2
            cnt2 += 1



print(cnt-1, cnt2-1)




