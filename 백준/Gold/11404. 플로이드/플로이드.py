INF = int(1e9)
# 도시의 수(노드)
n = int(input())

# 버스의 개수(간선)
m = int(input())

# 각 도시에 대한 버스 정보 배열 생성
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    # 출발 도시(a), 도착 도시(b), 비용(c)
    a, b, c = map(int, input().split())
    # 그래프 배열에 정보 저장
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()



