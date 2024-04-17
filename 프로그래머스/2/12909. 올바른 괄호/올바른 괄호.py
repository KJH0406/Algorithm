from collections import deque

def solution(s):
    answer = True
    s_list = deque([])
    for s_item in s:
        s_list.append(s_item)
    
    flag = 0
    
    while s_list:
        if flag < 0:
            answer = False
            break
        
        bracket = s_list.popleft()
        
        if bracket == '(':
            flag += 1
        else:
            flag -= 1
    
    if flag != 0:
        answer = False
        
    return answer