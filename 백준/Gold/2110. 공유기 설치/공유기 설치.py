import sys
input = sys.stdin.readline

n, c = map(int, input().split())  # N: 집의 개수, C : 설치해야 하는 공유기의 개수
house_list = [int(input()) for _ in range(n)]  # 집 리스트
house_list.sort()  # 이분탐색을 실행하기 전 반드시 오름차순 정렬


# gap 차이 이분 탐색
start = 1
end = house_list[-1]
gap = 0

while start <= end:
    mid = (start + end) // 2  # gap 값
    house = house_list[0]  # 처음 집과 거리 계산 시작
    cnt = 1  # 설치된 공유기 개수(배열의 가장 첫 집은 이미 설치)

    # 처음 집과 마지막 집을 제외한 나머지 집 탐색
    for i in range(1, n):

        # 설치가 가능한 집 = 마지막으로 설치된 집과 gap을 더했을 때 같거나 작다면
        if house_list[i] >= house + mid:
            house = house_list[i]  # 마지막으로 설치한 집 교체
            cnt += 1  # 설치 개수 증가

        # 만약 설치 된 개수가 많거나 같다면 gap을 조금 더 증가 시켜 판단
    if cnt >= c:
        start = mid + 1
        gap = mid  # 일단 결과 저장

        # 만약 해당 gap차이를 설정했을때 다 설치하지 못했다면 gap을 줄여야함
    else:
        end = mid - 1

print(gap)

















