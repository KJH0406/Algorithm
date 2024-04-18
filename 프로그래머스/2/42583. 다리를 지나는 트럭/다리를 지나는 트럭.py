def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    time = 1
    
    start_truck = truck_weights.pop(0)
    
    crossing_trucks = [0] * (bridge_length - 1) + [start_truck]
    
    flag_weight = weight - start_truck
    
    space = 0
    
    while crossing_trucks:
        flag_weight = min((flag_weight + crossing_trucks.pop(0)), weight)
        if truck_weights and truck_weights[0] <= flag_weight:
            for _ in range(space):
                crossing_trucks.append(0)
            enter_truck = truck_weights.pop(0)
            crossing_trucks.append(enter_truck)   
            space = 0
            flag_weight -= enter_truck
        else:
            space += 1
        time += 1
    
    
    
    answer = time
                
    
    return answer