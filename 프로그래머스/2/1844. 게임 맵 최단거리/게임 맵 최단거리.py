from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0, 0)])  # 시작 위치 초기화와 동시에 큐에 추가
    visited = [[0] * m for _ in range(n)] # 최단 거리를 기록할 방문 배열 생성
    visited[0][0] = 1  # 시작 지점 방문 표시
    
    while queue:
        ci, cj = queue.popleft()
        
        if ci == n - 1 and cj == m - 1:  # 목적지 도달 시 종료
            return visited[ci][cj]
        
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni, nj))
                
    return -1  # 목적지에 도달하지 못한 경우
