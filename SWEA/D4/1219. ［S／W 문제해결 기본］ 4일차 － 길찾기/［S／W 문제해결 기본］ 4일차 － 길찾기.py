for tc in range(1, 11):
    t, N = map(int, input().split())
    arr = [[0] * 100 for _ in range(100)]
    visited = [False] * 100
    stack = []
    numbers = list(map(int, input().split()))
    for i in range(0, N*2, 2):
        arr[numbers[i]][numbers[i+1]] = 1

    v = 0
    visited[v] = True

    while True:
        for w in range(100):
            if arr[v][w] == 1 and not visited[w]:
                stack.append(v)
                visited[w] = True
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

    if visited[99]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
        
'''
T = 10
for tc in range(1, T+1):
    t, E = map(int, input().split())

    graph = [[0] * 100 for _ in range(100)]  # 노드 연결을 표시할 빈 그래프 생성

    visited = [False] * 100  # 노드 방문을 기록할 초기값 설정

    stack = []  # 빈 스택 생성

    num_list = list(map(int, input().split()))
    # print(num_list)

    for i in range(0, E*2, 2):
        a = num_list[i]
        b = num_list[i+1]
        graph[a][b] = 1  # 두 점이 이어지도록 1로 변환
    S = 0
    G = 99
    # 2 차원 배열을 다 불러왔음.

    v = S  # 시작점 1로 설정
    visited[v] = True

    while True:
        for w in range(100):  # w는 도착점
            if graph[v][w] == 1 and not visited[w]:
                stack.append(v)  # 방문지로 넣어줌
                v = w  # 출발점을 현재 방문한곳 w로 바꿔줌
                visited[w] = True  # 방문했으니까 True로 바꿔줌
                break
        else:  # 아무것도 찾지못하고
            if stack:  # 스택에 아무것도 없으면
                v = stack.pop()
            else:  # 더이상 탐색할것이 없음
                break  # 전체 while문 종료

    if visited[99] == True: #도착점까지 갈 수 있다면
        print(f'#{tc} 1') # 1프린트
    else:
        print(f'#{tc} 0')
'''