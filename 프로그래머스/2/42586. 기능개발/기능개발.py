def solution(progresses, speeds):
    answer = []
    
    deploy_count = 1
    
    current_deploy_day = 0
    
    start_function = (progresses.pop(0), speeds.pop(0))
    
    flag = (100 - start_function[0]) % start_function[1]
    
    if flag == 0:
        current_deploy_day = (100 - start_function[0]) // start_function[1]
    else:
        current_deploy_day = (100 - start_function[0]) // start_function[1] + 1
    
    if progresses:
        while progresses:
            next_progress, next_speed = progresses.pop(0), speeds.pop(0)
            next_deploy_day = 0
            
            if (100 - next_progress) % next_speed == 0:
                next_deploy_day = (100 - next_progress) // next_speed 
            else:
                next_deploy_day = (100 - next_progress) // next_speed  + 1
            
            if next_deploy_day <= current_deploy_day:
                deploy_count += 1
            else:
                answer.append(deploy_count)
                current_deploy_day = next_deploy_day
                deploy_count = 1
        answer.append(deploy_count)     

    else:
        answer.append(1)
            
    
    return answer