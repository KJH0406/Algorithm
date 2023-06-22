from collections import deque

M, N, H = map(int, input().split())

queue = deque()
farm = []
for _ in range(H):
    farm.append([list(map(int, input().split())) for _ in range(N)])
for h in range(H):
    for i in range(N):
        for j in range(M):
            if farm[h][i][j] == 1:
                queue.append((h, i, j))
while queue:
    sh, si, sj = queue.popleft()
    for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
        nh, ni, nj = sh + dh, si + di, sj + dj
        if 0<= nh < H and 0 <= ni < N and 0 <= nj < M and farm[nh][ni][nj] == 0:
            queue.append((nh, ni, nj))
            farm[nh][ni][nj] = farm[sh][si][sj] + 1

res = 0
flag = 1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if farm[h][i][j] == 0:
                flag = 0
                break
            else:
                res = max(res, farm[h][i][j])
if flag:
    print(res - 1)
else:
    print(-1)
