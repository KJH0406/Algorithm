while True:
    N = int(input())
    if N == 0:
        break
    else:
        li = list(input().split(','))
        S = [0] * (N + 1)
        for item in li:
            if '-' in item:
                a, b = item.split('-')
                a = int(a)
                b = int(b)
                if a == b and a <= N and S[a] == 0:
                    S[a] = 1
                elif a < b:
                    for i in range(a, b+1):
                        if i <= N and S[i] == 0:
                            S[i] = 1
            else:
                item = int(item)
                if item <= N and S[item] == 0:
                    S[item] = 1
        print(S.count(1))