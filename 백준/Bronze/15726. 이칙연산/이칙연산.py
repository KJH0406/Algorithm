import math
a, b, c = map(int, input().split())
res = 0
if b > c:
    res = a * b / c

elif c > b:
    res = a * c / b

print(math.floor(res))
