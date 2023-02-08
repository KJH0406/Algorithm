case = 0
while True:
    count = 0
    case += 1
    char_list = list(input())
    if '-' in char_list:
        break
    else:
        stop = 0
        while True:
            if stop == len(char_list)-1:
                break
            elif len(char_list) == 0:
                break
            else:
                for i in range(len(char_list)-1):
                    if char_list[i] + char_list[i+1] == '{}':
                        char_list.pop(i)
                        char_list.pop(i)
                        stop = 0
                        break
                    else:
                        stop += 1
        for idx in range(0, len(char_list), 2):
            if char_list[idx] == '}':
                count += 1
                if char_list[idx+1] == '{':
                    count += 1
            else:
                if char_list[idx+1] == '{':
                    count += 1

        print(f'{case}. {count}')






