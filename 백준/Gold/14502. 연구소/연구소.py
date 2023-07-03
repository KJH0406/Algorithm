from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(N)]

ans = 0

def backtrack(n, board):
    global ans
    if n == 3:
        queue = deque()
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    queue.append((i, j))
                elif arr[i][j] == 1:
                    visited[i][j] = 1

        while queue:
            si, sj = queue.popleft()
            visited[si][sj] = 2
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 2
        cnt = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 0:
                    cnt += 1
        ans = max(ans, cnt)
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                backtrack(n+1, board)
                board[i][j] = 0

backtrack(0, arr)
print(ans)

