n = int(input())
for i in range(n):
    if i == 0:
        star = ' ' * (n - 1 - i) + '*' * (i + 1)
        star = (' ' * i).join(star)
        print(star)
    elif i == n-1:
        print('*' * (2 * n -1))
    else:
        space = ' ' * (n - 1 - i)
        star = '*' * 2
        star = (' ' * (i * 2 - 1)).join(star)
        print(space + star)


