T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    A_list.sort()
    B_list.sort()
    cnt = 0
    for item in A_list:
        l = 0
        r = M - 1
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if B_list[m] < item:
                ans = m
                l = m + 1
            else:
                r = m - 1
        cnt += ans + 1
    print(cnt)