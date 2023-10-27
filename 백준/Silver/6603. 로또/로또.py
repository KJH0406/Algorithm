import itertools

while True:

    arr = list(map(int, input().split()))

    k = arr[0]
    S = arr[1:]

    for i in itertools.combinations(S, 6):
        print(*i)

    if k == 0:
        exit()
    print()