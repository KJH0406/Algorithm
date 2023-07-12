N, M = map(int, input().split())
score = list(map(int, input().split()))
ans = []
for _ in range(M):
    person = list(input().split())
    s = 0
    for i in range(1, N+1):
        if person[i] == 'O':
            s += score[i-1]
    ans.append((int(person[0]), s))
ans.sort()

maxV = [0, 0]
for item in ans[::-1]:
    if maxV[1] <= item[1]:
        maxV = item
print(*maxV)

