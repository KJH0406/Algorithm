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

    for i in range(2, n + 1):
        if arr[i] == True and i != 1:
            res.append(i)

    for item in res:
        if n == item + item:
            s.append((item, item))
    if s:
        print(*s[0])
    else:
        for i in range(len(res)-1):
            for j in range(i+1, len(res)):
                if n == res[i] + res[j]:
                    s.append((res[i], res[j]))
        s.sort(key=lambda x: x[1]-x[0])
        print(*s[0])

