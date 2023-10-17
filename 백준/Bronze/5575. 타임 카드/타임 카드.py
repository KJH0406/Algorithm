for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    time1 = h1 * 60 * 60 + m1 * 60 + s1
    time2 = h2 * 60 * 60 + m2 * 60 + s2
    time = time2 - time1
    H = time //60//60 % 24
    M = time //60 % 60
    S = time %60
    print(H, M, S)