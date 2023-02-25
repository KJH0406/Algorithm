T = int(input())
for tc in range(1, T+1):
    t, N = input().split()
    numbers = list(input().split())
    res = []
    res2 = []
    N = int(N)
    dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    for item in numbers:
        for key, value in dic.items():
            if item == key:
                res.append(value)
    res.sort()
    for item in res:
        for key, value in dic.items():
            if item == value:
                res2.append(key)
    print(f'#{tc}')
    print(*res2)
