c, r = map(int, input().split())
k = int(input())
arr = [[0] * c for _ in range(r)]
rotation = 0
count = 1
si = 0
sj = 0
while True:
    if count >= c * r:
        break
    else:
        while True:  # 위로 증가
            if count == c * r:
                arr[si][sj] = count
                break
            else:
                if si == r-rotation-1:
                    arr[si][sj] = count
                    count += 1
                    sj += 1
                    break
                else:
                    arr[si][sj] = count
                    si += 1
                    count += 1
        while True:  # 오른쪽으로 증가
            if count == c * r:
                arr[si][sj] = count
                break
            else:
                if sj == c-rotation-1:
                    arr[si][sj] = count
                    count += 1
                    si -= 1
                    break
                else:
                    arr[si][sj] = count
                    sj += 1
                    count += 1
        while True:  # 아래쪽으로 감소
            if count == c * r:
                arr[si][sj] = count
                break
            else:
                if si == rotation:
                    arr[si][sj] = count
                    count += 1
                    sj -= 1
                    break
                else:
                    arr[si][sj] = count
                    si -= 1
                    count += 1
        while True:  # 왼쪽으로 증가
            if count == c * r:
                arr[si][sj] = count
                break
            else:
                if sj == rotation + 1:
                    arr[si][sj] = count
                    count += 1
                    sj -= 1
                    break
                else:
                    arr[si][sj] = count
                    sj -= 1
                    count += 1
        rotation += 1
        si += 1
        sj += 1


break_count = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == k:
            print(j+1, i+1)
            break_count += 1
            break
    if break_count == 1:
        break
else:
    print(0)
