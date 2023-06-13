T = int(input())

for _ in range(T):
    n = int(input())

    arr = [True] * (n + 1)
    res = []
    s = []
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if arr[i] == True:
            for j in range(i + i, n + 1, i):
                arr[j] = False

    count = 0
    for i in range(2, n // 2 + 1):
        if arr[i] and arr[n - i]:
            count += 1
    print(count)