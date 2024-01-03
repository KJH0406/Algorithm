N, M = map(int, input().split())  # N * M 의 방의 크기
r, c, d = map(int, input().split())  # r, c : 초기 로봇 청소기 위치, d : 방향
room = [list(map(int, input().split())) for _ in range(N)]  # 방의 상태

ans = 0  # 로봇 청소기가 있는 칸은 항상 빈 칸 이므로 한 칸은 무조건 청소를 하게됨.
coordinates = [(r, c)]  # 좌표 배열
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 방향

while coordinates:
    si, sj = coordinates.pop(0)  # 청소기 시작 좌표

    #  청소 되지 않은 빈 칸
    if room[si][sj] == 0:
        ans += 1  # 청소한 칸의 개수 증가
        room[si][sj] = 2  # 청소 완료

    # 4면 탐색
    for di, dj in direction:
        ni, nj = si + di, sj + dj  # 탐색 후 위치 좌표

        # 청소가 되지 않은 칸
        if room[ni][nj] == 0:
            # 반 시계로 방향 90도 회전
            if d == 0:
                d = 3
            else:
                d -= 1
           
            cdi, cdj = direction[d]
            
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            if room[si + cdi][sj + cdj] == 0:
                coordinates.append((si + cdi, sj + cdj))
                break
            # 아니면 제 자리에서 다시 4면 탐색
            else:
                coordinates.append((si, sj))
                break

    # 빈 칸이 없는 경우
    else:
        if d == 0 and room[si + 1][sj] != 1:
            coordinates.append((si + 1, sj))
        elif d == 1 and room[si][sj - 1] != 1:
            coordinates.append((si, sj - 1))
        elif d == 2 and room[si - 1][sj] != 1:
            coordinates.append((si - 1, sj))
        elif d == 3 and room[si][sj + 1] != 1:
            coordinates.append((si, sj + 1))
        else:
            break

print(ans)













