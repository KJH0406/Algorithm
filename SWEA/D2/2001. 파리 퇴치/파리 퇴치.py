T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    s = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for m in range(M):
                s += sum(arr[i+m][j:j+M])
            sum_list.append(s)
            s = 0

    print(f'#{tc} {max(sum_list)}')
