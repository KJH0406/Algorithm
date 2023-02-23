while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        arr2 = [[3] * (w+2)]
        arr = [[3] + list(map(int, input().split())) + [3] for _ in range(h)]
        arr = arr2 + arr + arr2
        visited = [[False] * (w+2) for _ in range(h+2)]
        stack = []
        count = 0

        for si in range(1, w+1):
            for sj in range(1, h+1):
                if arr[sj][si] == 1 and not visited[sj][si]:
                    stack.append((sj, si))
                    visited[sj][si] = True
                    count += 1
                    while stack:
                        y, x = stack.pop()
                        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                            ni, nj = x + di, y + dj
                            if arr[nj][ni] == 1 and not visited[nj][ni]:
                                stack.append((nj, ni))
                                visited[nj][ni] = True

        print(count)