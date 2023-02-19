T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr1 = [[0]*(N+2)]
    arr2 = [[0] + list(input()) + [0] for _ in range(N)]
    arr = arr1 + arr2 + arr1
    omok = 0
    for si in range(1, N+1):
        for sj in range(1, N+1):
            if arr[si][sj] != '.':
                for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    count = 0
                    for mul in range(1, N+1):
                        ni, nj = si + di * mul, sj + dj * mul
                        if arr[ni][nj] == 0:
                            break
                        elif arr[ni][nj] == 'o':
                            count += 1
                            if count >= 4:
                                omok += 1
                                break

                        else:
                            count = 0
                            break

    if omok > 0:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

