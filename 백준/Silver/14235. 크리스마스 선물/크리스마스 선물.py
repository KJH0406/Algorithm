import sys
input = sys.stdin.readline
N = int(input())
res = []
for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if res:
            res.sort()
            print(res.pop())
        else:
            print(-1)
    else:
        for i in range(1, len(a)):
            res.append(a[i])



