T = int(input())
for t in range(1, T+1):
    date = input()
    if date[5] == '2':
        if 1 <= int(date[6:]) <= 28:
            print(f'#{t} {date[0:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{t} -1')
    elif date[5] in '13456789':
            if 1 <= int(date[6:]) <= 32 :
                print(f'#{t} {date[0:4]}/{date[4:6]}/{date[6:]}')
            else:
                print(f'#{t} -1')
    else:
        print(f'#{t} -1')
