def sum_value(li):
    s = 0
    for item in li:
        s += item
    return s


for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []
    s = 0
    for i in range(100):
        s += arr[i][i]

    sum_list.append(s)

    s = 0
    for j in range(99, -1, -1):
        s += arr[99-j][j]
    sum_list.append(s)

    for i in range(100):
        sum_list.append(sum_value(arr[i]))

    for j in range(100):
        s = 0
        for i in range(100):
            s += arr[i][j]
        sum_list.append(s)

    print(f'#{tc} {max(sum_list)}')
