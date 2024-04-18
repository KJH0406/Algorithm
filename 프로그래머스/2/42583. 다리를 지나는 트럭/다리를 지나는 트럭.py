def solution(bridge_length, weight, truck_weights):
    answer = 0

    time = 1  # 소요 시간

    start_truck = truck_weights.pop(0)  # 처음 진입 하는 트럭

    crossing_trucks = [0] * (bridge_length - 1) + [start_truck]  # 다리를 건너고 있는 트럭

    current_bridge_weight = weight - start_truck  # 현재 다리가 견딜 수 있는 무게 판단

    time_space = 0  # 대기 간격 카운트

    while crossing_trucks:
        # 견딜 수 있는 원래의 최대 하중이 변형 되지 않도록 min 사용
        current_bridge_weight = min((current_bridge_weight + crossing_trucks.pop(0)), weight)
        
        # 진입 가능 여부 판단
        if truck_weights and truck_weights[0] <= current_bridge_weight:
            # 대기 간격 추가
            for _ in range(time_space):
                crossing_trucks.append(0)
            enter_truck = truck_weights.pop(0)  # 진입 가능한 트럭 추출
            crossing_trucks.append(enter_truck)  # 다리에 추가
            time_space = 0  # 대기 간격 초기화
            current_bridge_weight -= enter_truck  # 현재 다리 하중에 반영
        else:
            # 진입이 불가능 하다면 대기 간격 증가
            time_space += 1
        
        # 소요 시간 증가
        time += 1

    answer = time

    return answer