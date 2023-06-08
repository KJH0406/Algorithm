a, b = map(int, input().split())
A_list = set(list(map(int, input().split())))
B_list = set(list(map(int, input().split())))

res = list(A_list.difference(B_list))
res.sort()

if len(res) == 0:
    print(0)
else:
    print(len(res))
    print(' '.join(map(str, res)))

