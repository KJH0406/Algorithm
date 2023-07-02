from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[[0] * 2 for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0, 0, 0))
v[0][0][0] = 1

while queue:
    si, sj, p = queue.popleft()
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == 1 and p == 0:
                queue.append((ni, nj, 1))
                v[ni][nj][1] = v[si][sj][0] + 1
            elif arr[ni][nj] == 0 and v[ni][nj][p] == 0:
                queue.append((ni, nj, p))
                v[ni][nj][p] = v[si][sj][p] + 1


res = v[N-1][M-1]
if res[0] > 0 and res[1] > 0:
    print(min(res))
elif res[0] == 0 and res[1] == 0:
    print(-1)
else:
    print(max(res))
