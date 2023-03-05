padding = [[3] * 21]
arr = [[3] + list(map(int, input().split())) + [3] for _ in range(19)]
board = padding + arr + padding
res = []
for si in range(1, 20):
    for sj in range(1, 20):
        if board[si][sj] == 1:
            for di, dj in ((0, 1), (1, -1), (1, 0), (1, 1)):
                count = 1
                ni, nj = si + di, sj + dj
                while board[ni][nj] != 3 and board[ni][nj] != 2 and board[ni][nj] != 0:
                    count += 1
                    ni, nj = ni + di, nj + dj
                if count == 5 and board[si-di][sj-dj] != 1:
                    res.append((si, sj, di, dj, 1))
        if board[si][sj] == 2:
            for di, dj in ((0, 1), (1, -1), (1, 0), (1, 1)):
                count = 1
                ni, nj = si + di, sj + dj
                while board[ni][nj] != 3 and board[ni][nj] != 1 and board[ni][nj] != 0:
                    count += 1
                    ni, nj = ni + di, nj + dj
                if count == 5 and board[si-di][sj-dj] != 2:
                    res.append((si, sj, di, dj, 2))
if res:
    for x, y, xi, xj, p in res:
        if xi == 0 and xj == 1:
            print(p)
            print(x, y)
            break
        elif xi == 1 and xj == 0:
            print(p)
            print(x, y)
            break
        elif xi == 1 and xj == 1:
            print(p)
            print(x, y)
            break
        else:
            print(p)
            print(x + 4, y - 4)
            break
else:
    print(0)