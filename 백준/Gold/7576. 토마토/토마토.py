from collections import deque
queue = deque()

M, N = map(int, input().split())  # M:가로(column), N:세로(row)
farm = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            queue.append((i, j))
res = 0
while queue:
    si, sj = queue.popleft()
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and farm[ni][nj] == 0:
            queue.append((ni, nj))
            farm[ni][nj] = farm[si][sj] + 1


flag = 1
for i in range(N):
    for j in range(M):
        if farm[i][j] == 0:
            flag = 0
            break
        else:
            res = max(res, farm[i][j])
if flag:
    print(res - 1)
else:
    print(-1)




