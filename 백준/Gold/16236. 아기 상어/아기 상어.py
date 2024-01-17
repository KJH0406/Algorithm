from collections import deque

# 공간의 크기
n = int(input())

# 공간의 상태
board = [list(map(int, input().split())) for _ in range(n)]

# 해당 공간 방문 확인
visited = [[0] * n for _ in range(n)]

# 아기 상어 크기
baby_shark = 2

# 먹은 물고기의 수
cnt = 0

# 도움을 요청하지 않은 시간
time = 0

# 아기 상어의 초기 위치
si, sj = 0, 0

# 아기 상어 초기 위치 탐색
flag = 0
for i in range(n):
    # 아기 상어 찾았다면 반복 중지
    if flag == 1:
        break
    for j in range(n):
        if board[i][j] == 9:
            # 아기 상어 위치 정보 저장
            si, sj = i, j
            flag = 1
            break

queue = deque([(si, sj)])
visited[si][sj] = 1
board[si][sj] = 0

time_list = []

while queue:
    # 상어 크기 판단
    if baby_shark == cnt:
        baby_shark += 1
        cnt = 0

    # 아기 상어의 현재 위치
    ci, cj = queue.popleft()

    # 주변 탐색
    for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        ni, nj = ci + di, cj + dj

        # 해당 칸을 이동할 수 있는 경우
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] <= baby_shark and visited[ni][nj] == 0:
            queue.append((ni, nj))
            visited[ni][nj] = visited[ci][cj] + 1

            # 먹을 수 있는 물고기가 있을 경우
            if board[ni][nj] < baby_shark and board[ni][nj] != 0:
                time = visited[ni][nj]  # 해당 위치 까지 걸린 시간 기록
                time_list.append((time, ni, nj))

        if time_list:
            if time != time_list[0][0] or not queue:
                time_list.sort()
                pi, pj = time_list[0][1], time_list[0][2]
                cnt += 1  # 먹이 카운트 증가
                board[pi][pj] = 0  # 물고기를 빈 칸으로 변환
                visited = [[0] * n for _ in range(n)]  # 방문 배열 초기화
                visited[pi][pj] = time_list[0][0]  # 현재 위치 까지 걸린 시간을 통해 방문 여부 갱신
                queue = deque([(pi, pj)])  # 큐 초기화
                time_list = []
                break

if time:
    print(time - 1)
else:
    print(time)






