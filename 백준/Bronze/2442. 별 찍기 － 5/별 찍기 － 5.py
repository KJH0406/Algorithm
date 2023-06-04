N = int(input())

for i in range(N):
    star = ' ' * (N-1-i) + '*' * (2*i + 1)
    print(star)


    