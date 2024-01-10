from collections import deque

N, M, K, X = map(int, input().split())

roads = {}

for _ in range(M):
    A, B = map(int, input().split())
    if A in roads:
        roads[A].append(B)
    else:
        roads[A] = [B]

distance = [0] * (N + 1)

queue = deque()
queue.append(X)
distance[X] = 1

start = True

while queue:
    if start == True:
        distance[X] = 0
        start = False
    else:
        distance[X] = 1
    current = queue.popleft()
    if current in roads:
        for city in roads[current]:
            if distance[city] == 0:
                distance[city] = distance[current] + 1
                queue.append(city)

flag = 1
distance[X] = 0

for i in range(N + 1):
    if distance[i] == K:
        flag = 0
        print(i)

if flag:
    print(-1)




