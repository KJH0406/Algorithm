import heapq

V, E = map(int, input().split())
S = int(input())
INF = 987654321
arr = [[] for _ in range(V+1)]
D = [INF] * (V+1)

for _ in range(E):
    i, j, w = map(int, input().split())
    arr[i].append((w,j))

q = []
heapq.heappush(q, (0, S))
D[S] = 0
while q:
    c, n = heapq.heappop(q)
    if c > D[n]:
        continue
    D[n] = c

    for item in arr[n]:
        temp_d = c + item[0]
        if temp_d < D[item[1]]:
            D[item[1]] = temp_d
            heapq.heappush(q, (temp_d, item[1]))

for i in range(1, V+1):
    if D[i] != INF:
        print(D[i])
    else:
        print('INF')
