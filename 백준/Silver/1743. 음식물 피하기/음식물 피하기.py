N, M, K = map(int, input().split())  # N: 세로 길이 , M: 가로 길이, K: 음식물 쓰레기의 개수
arr = [['.'] * (M+2) for _ in range(N + 2)]  # 델타 탐색에서 인덱스 에러가 나지 않게 패딩해줌.

for _ in range(K):  # 음식물 쓰레기 개수만큼 반복
    r, c = map(int, input().split())  # 음식물 쓰레기 좌표값 받아옴
    arr[r][c] = '#'  # 해당 위치에 음식물 쓰레기 투척

food = 0  # 뭉친 음식물 쓰레기 중 가장 큰것을 갱신할 변수 생성
queue = []  # BFS 탐색 시 필요한 큐생성
visited = [[False] * (M+2) for _ in range(N+2)]  # 해당 위치 방문여부 표시할 리스트 생성
si = sj = 0  # 현 위치를 파악할 변수 생성

for i in range(1, N+1):  # 패딩 범위를 제외한 행 탐색
    for j in range(1, M+1):  # 패딩 범위를 제외한 열 탐색
        if arr[i][j] == '#':  # 만약 음식물 쓰레기가 있다면
            si, sj = i, j  # 해당 위치부터 탐색 시작
            queue.append((si, sj))  # 큐에 해당 좌표 넣어주고
            visited[si][sj] = True  # 방문 여부 바꿔줌
            cnt = 1  # 음식물 쓰레기 크기는 1부터 시작
            while queue:
                ci, cj = queue.pop(0)
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우 탐색
                    ni, nj = ci + di, cj + dj
                    if arr[ni][nj] == '#' and not visited[ni][nj]:  # 만약 상하좌우에 음식물쓰레기가 있고 방문하지 않았다면
                        queue.append((ni, nj)) # 큐에 넣어주면서 범위 확장
                        visited[ni][nj] = True
                        cnt += 1  # 음식물쓰레기 크기를 늘려줌
            if food < cnt:  # 만약 최대 음식물쓰레기 크기보다 크다면
                food = cnt  # 최대값 갱신
print(food)