def solution(friends, gifts):
    answer = 0
    
    n = 0
    
    friends_dic = {} # 친구 목록
    
    for friend in friends:
        friends_dic[friend] = n
        n += 1
    
    arr = [[0] * (n) for _ in range(n)]  # 주고 받은 선물 배열
    gift_info = [[0, 0, 0] for _ in range(n)]  # 최종 선물 정보 배열
    
    res = [0] * n # 다음달 받을 선물 정보 
    
    for gift in gifts:
        give, receive = gift.split(' ')
        give, receive = friends_dic[give], friends_dic[receive]
        
        arr[give][receive] += 1  # 주고 받은 선물 정보 입력
        
        gift_info[give][0] += 1 # 준 사람의 준 선물 수 증가
        gift_info[receive][1] += 1 # 받은 사람의 받은 선물 증가
        
        gift_info[give][2] += 1 # 준 사람의 선물 지수 증가
        gift_info[receive][2] -= 1 # 받은 사람의 선물 지수 감소
    
    
    for i in range(n):
        for j in range(n):
            if i < j:
                # 서로 선물을 주고 받은 기록이 없다면
                if (arr[i][j] == 0 and arr[j][i] == 0) or arr[i][j] == arr[j][i]:
                    # 선물지수가 더 큰 사람이 작은 사람에게 1개의 선물을 받음
                    if gift_info[i][2] > gift_info[j][2]:
                        res[i] += 1
                    elif gift_info[i][2] < gift_info[j][2]:
                        res[j] += 1
                else:
                    if arr[i][j] > arr[j][i]:
                        res[i] += 1
                    else:
                        res[j] += 1
    
                
    answer = max(res)
            
    return answer