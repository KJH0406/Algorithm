for tc in range(1, 11):
    t = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    sj_list = []
    res = []
    for j in range(101):
        if arr[0][j] == 1:
            sj_list.append(j)

    for i in sj_list:
        sj = i
        si = 0
        count = 0
        while si < 99:
            if arr[si][sj-1] == 0 and arr[si][sj+1] == 0:
                si += 1
            elif arr[si][sj-1] == 1:
                while arr[si][sj-1] == 1:
                    sj -= 1
                    count += 1
                si += 1
            elif arr[si][sj+1] == 1:
                while arr[si][sj+1] == 1:
                    sj += 1
                    count += 1
                si += 1
        res.append((count, i))
    res.sort(key=lambda x: (x[0], -x[1]))
    print(f'#{tc} {res[0][1]-1}')





