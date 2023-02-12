T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    count_list = []
    count = 1
    for i in range(N-1):
        if num_list[i] < num_list[i+1]:
            count += 1
        else:
            count_list.append(count)
            count = 1
    count_list.append(count)
    for i in range(len(count_list)-1):
        for j in range(i+1, len(count_list)):
            if count_list[i] < count_list[j]:
                count_list[i], count_list[j] = count_list[j], count_list[i]
    print(f'#{tc} {count_list[0]}')

'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split())) # 공백을 기준으로 스플릿을 하고 list를 만들어줌
    count = 0   #연속된 값의 개수를 나타내기 위한 변수 count를 0으로 정의함
    count_list = [] # 연속된 값의 개수인 count를 저장할 list를 만들음.
    max_count = 0   # 가장 연속 된 값이 많은 것을 나타낼 변수를 만들어줌.
    for i in range(n-1): # 비교할 마지막 값을 지정해줌(n-1) 맨뒤에서 앞까지만 비교하면 되므로
        if num_list[i] + 1 == num_list[i+1]:
            count += 1  #만약 i번째에서 +1 더한 값이 i+1번째 값이랑 같으면 연속된 값이므로 count에 1을 더해줌
        else:
            count_list.append(count) # 연속이 끊기면 count_list에 count 값을 더해주고
            count = 0 # count값을 0으로 초기화해줌
            #위 과정을 거치면 연속된 값이 계속해서 count_list에 저장됨
    count_list.append(count) #for 문이 끝났을때 연속된 상태로 끝나서 else의 append를 거치지 않는 경우도 있으므로 count를 추가해줌.
    for j in count_list: #연속된 값이 담겨있는 count_list에서 요소를 꺼내옴
            if j > max_count:
                max_count = j #연속된 값중 가장 큰 값을 max_count로 바꿔줌
    print(f'#{tc} {max_count + 1}') #예를들어 234가 연속됐을 경우 max count는 2와3을 비교해서 +1, 3과 4를 비교해서 +1이 된 2인 상태이므로 +1을 해서 연속된 숫자의 개수를 구해줌.
'''