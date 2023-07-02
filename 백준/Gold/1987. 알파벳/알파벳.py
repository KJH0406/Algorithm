import sys
input = lambda: sys.stdin.readline().rstrip()

# dic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}


def dfs(si, sj, cnt):
    global ans
    ans = max(ans, cnt)
    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < R and 0 <= nj < C and visited[ord(arr[ni][nj])] == 0:
            visited[ord(arr[ni][nj])] = 1
            dfs(ni, nj, cnt + 1)
            visited[ord(arr[ni][nj])] = 0


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [0] * 128
visited[ord(arr[0][0])] = 1
ans = 1
dfs(0, 0, 1)
print(ans)