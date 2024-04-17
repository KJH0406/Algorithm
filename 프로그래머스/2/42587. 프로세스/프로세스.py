from collections import deque

def solution(priorities, location):
    answer = 0
    
    process_list = list(range(len(priorities)))
    
    # 우선 순위 최대 값 확인을 위한 오름차순 정렬
    max_value_list = sorted(priorities)
    
    
    queue = deque(list(zip(process_list, priorities)))
    
    
    while queue:
        # 우선 순위 최대 값
        max_value = max_value_list[-1]
        
        current_process, current_priority = queue.popleft()
        
        
        if max_value <= current_priority:
            max_value_list.pop()
            answer += 1
            if current_process == location:
                return answer
        else:
            queue.append((current_process, current_priority))
        