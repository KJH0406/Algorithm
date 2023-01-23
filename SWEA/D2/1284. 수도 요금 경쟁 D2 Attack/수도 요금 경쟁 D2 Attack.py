T = int(input())

for i in range(1, T + 1):
    money = 0
    num_list = list(map(int, input().split()))
    if num_list[4] < num_list[2]:
        if num_list[0] * num_list[4] <  num_list[1]:
            print(f'#{i} {num_list[0] * num_list[4]}')
        else:
            print(f'#{i} {num_list[1]}')
    else:
        if num_list[0] * num_list[4] <  num_list[1] + ((num_list[4] - num_list[2]) * num_list[3]):
            print(f'#{i} {num_list[0] * num_list[4]}')
        else:
            print(f'#{i} {num_list[1] + ((num_list[4] - num_list[2]) * num_list[3])}')


            


    
