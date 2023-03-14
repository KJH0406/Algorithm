N = int(input())
arr = []

for i in range(N-1, 0, -1):
    a = ' ' * i + '*' * (2 * (N-i) -1)
    arr.append(a)

arr.append('*' * (2 * N - 1))

for i in range(1, N):
    a = ' ' * i + '*' * (2 * (N-i) -1)
    arr.append(a)

for item in arr:
    print(item)
