n = int(input())
a = 0
b = 0
for _ in range(n):
    ai, bi = map(int, input().split())
    if ai > bi:
        a += (ai + bi)
    elif ai < bi:
        b += (ai + bi)
    else:
        a += ai
        b += bi
print(a, b)