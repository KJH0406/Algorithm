N = int(input())

for i in range(N-1, -1, -1):
    star = ' ' * (N-1-i) + '*' * (2*i + 1)
    print(star)


