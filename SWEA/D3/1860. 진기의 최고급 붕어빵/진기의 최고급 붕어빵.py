T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    person = list(map(int, input().split()))
    person.sort()
    s = 0
    for i in range(0, person[-1]+1):
        if i != 0 and i % M == 0:
            s += K
        if i in person:
            s -= 1
        if s < 0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')


