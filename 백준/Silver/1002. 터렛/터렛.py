
import math


t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    ans = abs(r1 - r2)
    rs = r1 + r2
    if d == 0 and r1 == r2:
        print(-1)
    elif ans == d or rs == d:
        print(1)
    elif ans < d < rs:
        print(2)
    else:
        print(0)