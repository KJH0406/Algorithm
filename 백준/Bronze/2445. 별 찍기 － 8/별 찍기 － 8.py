N = int(input())

for i in range(1, N+1):
    star = '*' * i + ' ' * (2 * N - 2 * i)
    star += '*' * i
    print(star)

for i in range(N-1, 0, -1):
    star = '*' * i + ' ' * (2 * N - 2 * i)
    star += '*' * i
    print(star)


