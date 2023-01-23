T = int(input())

for i in range(1, T+1):
    sum_result = 0
    num_list = list(map(int, input().split()))
    for num in num_list:
        sum_result += num
    print(f'#{i} {round(sum_result/len(num_list))}')  #round 함수를 통해서 반올림을 해준다.