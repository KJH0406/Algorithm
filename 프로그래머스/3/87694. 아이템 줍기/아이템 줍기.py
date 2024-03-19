from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 빈 공간 계산을 위해 변수 두배 처리
    si = characterX * 2
    sj = characterY * 2
    ti = itemX * 2
    tj = itemY * 2

    arr = [[0] * 102 for _ in range(102)]

    queue = deque([(si, sj)])

    visited = [[0] * 102 for _ in range(102)]

    visited[si][sj] = 1


    # 직사각형 도형 채우기
    for rectangle_coordinate_list in rectangle:
        x1, y1, x2, y2 = rectangle_coordinate_list
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                arr[i][j] = 1

    # 테두리를 제외한 공간 제거
    for rectangle_coordinate_list in rectangle:
        x1, y1, x2, y2 = rectangle_coordinate_list
        for i in range(x1 * 2 + 1, x2 * 2):
            for j in range(y1 * 2 + 1, y2 * 2):
                arr[i][j] = 0

    # BFS 탐색
    while queue:
        ci, cj = queue.popleft()

        if ci == ti and cj == tj:
            break

        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 1 <= ni <= 101 and 1 <= nj <= 101 and visited[ni][nj] == 0 and arr[ni][nj] != 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    
    # 초기 빈공간 계산을 위한 2배 처리 복구 (나누기 2)
    answer = (visited[ti][tj] - 1) // 2

    return answer
