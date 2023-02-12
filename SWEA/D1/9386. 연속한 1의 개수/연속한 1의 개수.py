def len_counting(li):
    count = 0
    for _ in li:
        count += 1
    return count

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(input().split('0'))
    max_len = 0
    for i in num_list:
        if max_len < len_counting(i):
            max_len = len_counting(i)
    print(f'#{tc} {max_len}')