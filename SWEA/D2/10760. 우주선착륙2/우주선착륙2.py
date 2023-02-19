T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = [[99] * (M+2)]
    arr2 = [[99] + list(map(int, input().split())) + [99] for _ in range(N)]
    arr = arr1 + arr2 + arr1
    place = 0

    for si in range(1, N+1):
        for sj in range(1, M+1):
            count = 0
            for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                ni, nj = si + di, sj + dj
                if arr[ni][nj] < arr[si][sj]:
                    count += 1
                if count >= 4:
                    place += 1
                    break

    print(f'#{tc} {place}')

'''
N, M = map(int, input().split())  # 행: N, 열: M

    arr = [[99] + list(map(int, input().split())) + [99] for _ in range(N)]  # 양 옆에 패딩해줌, 안전하게 아에 높은 숫자 99로 패딩
    arr = [[99] * (M+2)] + arr + [[99] * (M+2)]  # 맨 위,아래 패딩해줌.

    candidate_area = 0  # 후보지 카운트 변수 생성


    for si in range(1, N + 1): # si, sj의 범위는 arr이 99로 패딩되어 있으니까 시작범위 인덱스는 0번째 인덱스에 있을 99를 제외한 1부터 시작
        for sj in range(1, M + 1):  # 끝 범위도 마찬가지로 N+1까지 설정하면 인덱스는 N까지 해당하므로 N+1인 99를 제외한 범위까지 반복
            low_area_count = 0  # 현재위치(si, sj)가 바뀔때마다 낮은 지역을 카운트해주어야 하므로 낮은지역 카운트를 0으로 초기화
            for di, dj in ((-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)):
                            # 좌상      상     우상      좌      우     좌하     하     우하
                ni = si + di  # 다음 위치의 행값(ni) = 현재위치의 행값(si) + 델타탐색을 통해 움직인 행값(di)
                nj = sj + dj  # 다음 위치의 열값(nj) = 현재위치의 열값(sj) + 델타탐색을 통해 움직인 열값(dj)
                if arr[ni][nj] < arr[si][sj]:  # 만약 델타탐색을 통한 위치가(ni, nj) 현재 위치(si, sj)보다 낮다면
                    low_area_count += 1  # 착륙지보다 낮은 지역이므로 카운트 +1 해줌
                    if low_area_count >= 4:  # 착륙지 높이보다 낮은지역이 4곳"이상"이면 후보지이므로(4개면 더이상 계산 필요없음)
                        candidate_area += 1  # 후보지에 1을 더해주고
                        break  # 델타 탐색을 마침

    print(f'#{tc} {candidate_area}')  # 후보지를 프린트해줌.
'''
