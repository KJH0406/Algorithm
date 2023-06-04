N = int(input())
for i in range(N, 0, -1):
    star = ' ' * (N - i) + '*' * (2 * i - 1)
    print(star)
for i in range(2, N+1):
    star = ' ' * (N - i) + '*' * (2 * i - 1)
    print(star)
