T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = round(N ** (1/3))
    if a ** 3 == N:
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} -1')

