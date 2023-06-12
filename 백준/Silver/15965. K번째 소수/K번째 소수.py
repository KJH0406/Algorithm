k = int(input())
M, N = 2, 8000000

arr = [True] * (N+1)

m = int(N ** 0.5)

for i in range(2, m+1):
    if arr[i] == True:
        for j in range(i+i, N+1, i):
            arr[j] = False
cnt = []
for i in range(M, N+1):
    if arr[i] == True and i != 1:
        cnt.append(i)

print(cnt[k-1])
