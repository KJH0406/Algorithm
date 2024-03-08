from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)  # 세로 길이
    m = len(maps[0])  # 가로 길이
    
    queue = deque()  
    
    visited = [[0] * m for _ in range(n) ]  # 최단 거리 저장 배열
    
    si = sj = 0 # 출발 지점
    
    visited[si][sj] = 1  # 출발 지점 거리 지정
    
    queue.append((si, sj))  # 출발 지점 큐에 추가
    
    while queue:
        ci, cj = queue.popleft() # 현재 위치
        
        # 델타 탐색
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci + di, cj + dj
            
            # 탐색 조건 체크
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1  # 최단 거리 기록
        
        # 상대 팀 진영 도달 여부 확인
        if visited[n - 1][m - 1]:
            answer = visited[n - 1][m - 1]
        else:
            answer = -1
                    
    return answer