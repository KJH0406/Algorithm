number = list(map(int, input()))
if len(number) == 1:
    if sum(number) in (3, 6, 9):
        print(0)
        print('YES')
    else:
        print(0)
        print('NO')
else:
    cnt = 1
    while sum(number) >= 10:
        number = sum(number)
        number = list(map(int, str(number)))
        cnt += 1

    if sum(number) in (3, 6, 9):
        print(cnt)
        print('YES')
    else:
        print(cnt)
        print('NO')
