N = int(input())  # 보드의 크기
board = [[3] * (N + 2)] + [[3] + [0] * N + [3] for _ in range(N)] + [[3] * (N + 2)]  # 보드 생성

K = int(input())  # 사과의 개수
for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 1

L = int(input())  # 방향 전환 횟수
direction_info = {}  # 방향 전환 정보
rotation_time = []  # 방향 전환 하는 시간
for _ in range(L):
    X, C = input().split()
    direction_info[int(X)] = C
    rotation_time.append(int(X))

time = 0  # 시간
si, sj = 1, 1  # 뱀의 현 위치
board[si][sj] = 2  # 보드에서 뱀 표시
rotation = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
d = 1  # 처음 에는 오른 쪽을 향해 시작(동쪽[1])

snake_length = [(si, sj)]


while True:
    time += 1
    di, dj = rotation[d]  # 이동 방향에 따른 좌표 설정
    ci, cj = snake_length[-1]
    ni, nj = ci + di, cj + dj  # 다음 이동 좌표

    # 이동 가능한 좌표일 시
    if N >= ni > 0 and N >= nj > 0 and board[ni][nj] < 2:
        # 해당 위치가 빈칸일 때
        if board[ni][nj] == 0:
            pi, pj = snake_length.pop(0)
            board[pi][pj] = 0
        board[ni][nj] = 2
        snake_length.append((ni, nj))

    # 이동 불가능 시 게임 종료
    else:
        break

    if time in rotation_time:
        if direction_info[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4

print(time)

