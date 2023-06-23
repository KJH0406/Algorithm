from collections import deque

N, K = map(int, input().split())
point = list(range(100001))
visited = [0] * 100001

queue = deque()
queue.append(N)
visited[N] = 1

flag = True
res = 0

while flag:
    cp = queue.popleft()
    if cp == K:
        flag = False
    else:
        for np in (cp + 1, cp - 1, cp * 2):
            if 0 <= np <= 100000 and visited[np] == 0:
                queue.append(np)
                visited[np] = visited[cp] + 1
print(visited[K] - 1)



