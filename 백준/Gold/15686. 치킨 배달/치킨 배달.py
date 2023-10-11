from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
ans = 9999

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

C_list = list(combinations(chicken, M))

for chi in C_list:
    temp = 0
    for h in house:
        c_res = 999
        H1, H2 = h
        for j in range(M):
            C1, C2 = chi[j]
            c_res = min(c_res, abs(H1 - C1) + abs(H2 - C2))
        temp += c_res
    ans = min(ans, temp)

print(ans)
