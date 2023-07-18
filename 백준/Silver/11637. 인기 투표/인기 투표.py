T = int(input())
for _ in range(T):
    N = int(input())
    temp = []
    for i in range(1, N+1):
        score = int(input())
        temp.append(score)
    maxV = max(temp)
    if temp.count(maxV) >= 2:
        print('no winner')
    else:
        if sum(temp) / 2 < maxV:
            print(f'majority winner {(temp.index(maxV) + 1)}')
        elif sum(temp) / 2 >= maxV:
            print(f'minority winner {(temp.index(maxV) + 1)}')

