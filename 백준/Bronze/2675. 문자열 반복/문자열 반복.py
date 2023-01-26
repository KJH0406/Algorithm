T = int(input())
for _ in range(T):
    R, alpha = input().split()
    for i in alpha:
        print(i * int(R), end='')
    print()