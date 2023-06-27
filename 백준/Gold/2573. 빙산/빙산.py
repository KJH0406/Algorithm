from collections import deque
def slice_check(lst, N, M):
    temp = deque()
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0:
                temp.append((i, j))
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i, j in temp:
        if visited[i][j] == 0:
            cnt += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = cnt
            while queue:
                si, sj = queue.popleft()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] != 0 and visited[ni][nj] == 0:
                        queue.append((ni, nj))
                        visited[ni][nj] = cnt
    return cnt

def zero_check(lst, N, M):
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0:
                return 1
    return 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    if slice_check(arr, N, M) >= 2:
        print(ans)
        break
    elif zero_check(arr, N, M) == 0:
        print(0)
        break
    else:
        box = deque()
        minus = deque()
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    box.append((i, j))
                    cnt = 0
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                            cnt += 1
                    minus.append(cnt)
        for i in range(len(box)):
            si, sj = box[i]
            arr[si][sj] = max(arr[si][sj] - minus[i], 0)
    ans += 1


