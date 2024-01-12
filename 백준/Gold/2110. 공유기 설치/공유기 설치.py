import sys
input = sys.stdin.readline

# n: 집의 개수, c : 설치 해야 하는 공유기의 개수
n, c = map(int, input().split())

# n개의 집의 좌표 정보 배열
house_list = [int(input()) for _ in range(n)] 

# 이분 탐색을 실행을 위한 정렬
# * 이분 탐색을 위한 사전 조건 입니다. 반드시 수행 하셔야 합니다!
house_list.sort()  

# 이분 탐색 실행을 위한 조건 설정
min_gap = 1  # 최소 거리 차이
max_gap = house_list[-1] - house_list[0]  # 최대 거리 차이

res = 0  # 결과 값

# 이분 탐색 실행
while min_gap <= max_gap:
    current_gap = (min_gap + max_gap) // 2  # 현재 가장 인접 한 두 공유기의 거리
    installed_house = house_list[0]  # 공유기를 설치한 집
    count = 1  # 설치된 공유기 개수

    # 배열의 가장 처음 집과 마지막 집을 제외한 나머지 범위 탐색
    for i in range(1, n):
        # 현재 탐색하고 있는 집이 이전에 설치 된 집과 현재 거리 차이를 더한 것 보다 같거나 크다면 설치 가능
        if house_list[i] >= installed_house + current_gap:
            installed_house = house_list[i]  # 가장 최신에 공유기를 설치한 집 교체
            count += 1  # 설치된 공유기 개수 증가


    # 위 과정을 실행 후 현재 거리 차이로 설치할 수 있는 공유기의 개수로 향후 거리 차이 증감 판단

    # 만약 설치 된 공유기의 개수(count)가 설치 해야 하는 공유기의 개수(c)보다 많거나 같다면 거리 차이 증가 가능
    if count >= c:
        min_gap = current_gap + 1  # 최소 거리 차이를 현재 거리 차이에서 1 증가된 값으로 변경
        res = current_gap  # 현재 거리 차이 저장

        # 만약 현재 거리 차이에서 공유기를 다 설치하지 못했다면 공유기 간 거리 차이를 줄여야 함
    else:
        max_gap = current_gap - 1  # 최대 거리 차이를 현재 거리 차이에서 1 감소된 값으로 변경

print(res)

















