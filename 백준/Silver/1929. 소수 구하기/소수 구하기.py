M, N = map(int, input().split())

arr = [True] * (N+1)

m = int(N ** 0.5)

for i in range(2, m+1):
    if arr[i] == True:
        for j in range(i+i, N+1, i):
            arr[j] = False

for i in range(M, N+1):
    if arr[i] == True and i != 1:
        print(i)

