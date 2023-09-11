a = int(input())
b = int(input())
res = 0
if a >= 20:
    res = 24 - a
    print(res + b)
else:
    b -= a
    print(b)



