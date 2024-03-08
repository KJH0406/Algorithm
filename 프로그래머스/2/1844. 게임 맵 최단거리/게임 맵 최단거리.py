from collections import deque

INF = 9876543210

def solution(maps):
    answer = 0
    
    n = len(maps)  # 세로 길이
    m = len(maps[0])  # 가로 길이
    
    queue = deque()  
    visited = [[0] * m for _ in range(n) ]  # 방문 여부 확인 배열
    
    si = sj = 0 # 출발 지점
    
    visited[si][sj] = 1  # 출발 지점 방문 체크
    queue.append((si, sj))  # 출발 지점 큐에 추가
    
    while queue:
        ci, cj = queue.popleft()
        
        # 델타 탐색
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    
        if visited[n - 1][m - 1]:
            answer = visited[n - 1][m - 1]
        else:
            answer = -1
                    
    return answer