def solution(friends, gifts):
    answer = 0
    
    n = len(friends)  # 친구의 수
    
    # 친구 목록을 인덱스로 매핑합니다.
    friends_dict = {friend: idx for idx, friend in enumerate(friends)}
    
    # 주고받은 선물 기록
    gift_exchange = [[0] * n for _ in range(n)]
    
    # 각 친구별로 준 선물 수, 받은 선물 수, 선물 지수를 관리합니다.
    gift_stats = [[0, 0] for _ in range(n)]  # [준 선물 수, 받은 선물 수]
    
    # 선물 기록을 바탕으로 데이터를 업데이트합니다.
    for gift in gifts:
        giver, receiver = gift.split(' ')
        giver_idx, receiver_idx = friends_dict[giver], friends_dict[receiver]
        
        gift_exchange[giver_idx][receiver_idx] += 1
        gift_stats[giver_idx][0] += 1  # 준 선물 수 증가
        gift_stats[receiver_idx][1] += 1  # 받은 선물 수 증가
    
    # 다음 달에 받을 선물 수를 계산합니다.
    next_month_gifts = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            # 선물 지수 계산
            gift_index_i = gift_stats[i][0] - gift_stats[i][1]
            gift_index_j = gift_stats[j][0] - gift_stats[j][1]
            
            # 선물 교환 기록이 있거나 선물 지수에 따라 결정
            if gift_exchange[i][j] > gift_exchange[j][i]:
                next_month_gifts[i] += 1
            elif gift_exchange[i][j] < gift_exchange[j][i]:
                next_month_gifts[j] += 1
            else:  # 선물을 주고받은 기록이 같거나 없는 경우
                if gift_index_i > gift_index_j:
                    next_month_gifts[i] += 1
                elif gift_index_i < gift_index_j:
                    next_month_gifts[j] += 1
    
    # 가장 많은 선물을 받을 친구가 받을 선물의 수를 반환합니다.
    answer = max(next_month_gifts)
    
    return answer