T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 보드판 크기 M: 돌놓는 횟수
    board = [[0] * (N+2) for _ in range(N+2)]
    board[N//2][N//2], board[N//2+1][N//2+1] = 2, 2
    board[N//2 + 1][N // 2], board[N // 2][N // 2 + 1] = 1, 1

    for _ in range(M):
        si, sj, d = map(int, input().split())
        board[si][sj] = d
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (1, 0), (0, 1), (1, 1), (1, -1), (0, -1)):
            temp = []
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul
                if board[ni][nj] == 0:
                    break
                elif board[ni][nj] != d:
                    temp.append((ni, nj))
                else:
                    for a, b in temp:
                        board[a][b] = d
                    temp = []
                    break

    black = 0
    white = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')





