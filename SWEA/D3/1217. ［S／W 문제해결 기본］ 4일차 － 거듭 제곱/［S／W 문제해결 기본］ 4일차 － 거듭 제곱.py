def square(n, m):
    if m == 1:
        return n
    else:
        return n * square(n, m-1)


for tc in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    print(f'#{t}', square(n, m))
