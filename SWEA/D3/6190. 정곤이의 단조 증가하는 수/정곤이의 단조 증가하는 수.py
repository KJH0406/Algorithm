T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    res = []

    for k in range(N-1):
        for j in range(N-1, k, -1):
            res.append(numbers[k] * numbers[j])
    res.sort(reverse=True)
    count = 0
    for num in res:
        num = str(num)
        for i in range(len(num)-1):
            if int(num[i]) > int(num[i+1]):
                break
        else:
            count += 1
            print(f'#{tc} {num}')
            break
    if count == 0:
        print(f'#{tc} -1')
