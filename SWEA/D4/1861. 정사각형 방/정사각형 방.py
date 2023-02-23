T = int(input())
for tc in range(1, T+1):
    N = int(input())
    padding = [[0] * (N+2)]
    room1 = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    room = padding + room1 + padding
    res = []
    stack = []

    for si in range(1, N+1):
        for sj in range(1, N+1):
            visited = [[0] * (N + 2) for _ in range(N + 2)]
            stack.append((si, sj))
            visited[si][sj] = 1
            count = 1
            while stack:
                x, y = stack.pop()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = x + di, y + dj
                    if room[ni][nj] != 0 and visited[ni][nj] == 0 and room[x][y] + 1 == room[ni][nj]:
                        stack.append((ni, nj))
                        visited[ni][nj] = 1
                        count += 1
            res.append((count, room[si][sj]))

    res.sort(key=lambda x:(-x[0], x[1]))

    print(f'#{tc} {res[0][1]} {res[0][0]}')






