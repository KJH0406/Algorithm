from collections import deque

N, M, K, X = map(int, input().split())

roads = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0
queue = deque([X])

while queue:
    current = queue.popleft()
    for city in roads[current]:
        if distance[city] == -1:
            distance[city] = distance[current] + 1
            queue.append(city)

flag = 1

for i in range(N + 1):
    if distance[i] == K:
        flag = 0
        print(i)

if flag:
    print(-1)




