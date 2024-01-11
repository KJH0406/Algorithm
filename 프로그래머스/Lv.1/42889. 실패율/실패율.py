def solution(N, stages):
    challenging = [0] * (N + 1)  # 도전 중인 사용자
    reach = [0] * (N + 1)  # 도달한 사용자

    for user in stages:  # 각 스테이지의 사용자 정보 추출
        
        # 사용자가 현재 도전 중인 스테이지에 추가
        if user <= N:
            challenging[user] += 1  
        
         # 도달한 스테이지 추가
        if user > N:
            for i in range(1, N + 1):
                reach[i] += 1
        else:
            for i in range(1, user + 1):
                reach[i] += 1
    temp = []
    answer = []
    for i in range(1, N + 1):
        if reach[i]:
            temp.append(((challenging[i] / reach[i]), i))
        else:
            temp.append((0, i))
    temp.sort(key = lambda x: (-x[0], x[1]))
    
    for i in range(N):
        answer.append(temp[i][1])    
    
    return answer