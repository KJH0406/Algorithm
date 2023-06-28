from collections import deque

F, S, G, U, D = map(int, input().split())

if S > G and D == 0:
    print('use the stairs')
elif S < G and U == 0:
    print('use the stairs')
else:
    visited = [1] + [0] * (F)
    queue = deque()
    queue.append(S)
    visited[S] = 1
    while queue:
        sp = queue.popleft()
        up = sp + U
        down = sp - D
        if 0 < up <= F and visited[up] == 0:
            queue.append(up)
            visited[up] = visited[sp] + 1
        if 0 < down <= F and visited[down] == 0:
            queue.append(down)
            visited[down] = visited[sp] + 1
        if up == G or down == G:
            break
    if visited[G] == 0:
        print('use the stairs')
    else:
        print(visited[G]-1)

