T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lotto = list(map(int, input().split()))
    max_price = lotto[-1]
    profit = 0
    
    for i in range(N-2, -1, -1):
        if max_price < lotto[i]:
            max_price = lotto[i]
        else:
            profit += max_price - lotto[i]
    
    print(f'#{tc} {profit}')




'''
count = 0
    profit = 0
    for i in range(N-1):
        if lotto[i] >= lotto[i+1]:
            count += 1
        else:
            break
    if count == len(lotto)-1:
        print(f'#{tc} 0')
    else:
        for i in range(N-1):
            if lotto[i] < max(lotto[i+1:]):
                profit += max(lotto[i+1:]) - lotto[i]
            else:
                pass
        print(f'#{tc} {profit}')
'''