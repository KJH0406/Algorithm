T = int(input())
a = 100
b = 100
for _ in range(T):
    t1, t2 = map(int, input().split())
    if t1 > t2:
        b -= t1
    elif t1 < t2:
        a -= t2

print(a)
print(b)