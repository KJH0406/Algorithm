n = int(input())
for i in range(n):
    if i == 0:
        star = ' ' * (n - 1 - i) + '*' * (i + 1)
        star = (' ' * i).join(star)
        print(star)
    else:
        space = ' ' * (n - 1 - i)
        star = '*' * (i+1)
        star = ' '.join(star)
        print(space + star)


