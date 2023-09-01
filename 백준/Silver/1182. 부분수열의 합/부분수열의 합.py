from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    temp = combinations(arr, i)
    for item in temp:
        if sum(item) == S:
            cnt += 1
print(cnt)