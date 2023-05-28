T = int(input())
for _ in range(T):
    a, b = input().split()
    ta = list(a)
    tb = list(b)
    ta.sort()
    tb.sort()

    if len(ta) != len(tb):
        print(f'{a} & {b} are NOT anagrams.')
    else:
        cnt = 0
        for i in range(len(ta)):
            if ta[i] != tb[i]:
                cnt += 1
        if cnt != 0:
            print(f'{a} & {b} are NOT anagrams.')
        else:
            print(f'{a} & {b} are anagrams.')