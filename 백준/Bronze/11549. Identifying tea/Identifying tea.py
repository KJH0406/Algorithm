N = int(input())
cnt = 0
li = list(map(int, input().split()))
for item in li:
    if item == N:
        cnt += 1
print(cnt)