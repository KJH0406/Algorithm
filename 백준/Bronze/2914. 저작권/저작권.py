import math
a, b = map(int, input().split())
i = 1
while True:
    if b == math.ceil(i / a):
        print(i)
        break
    else:
        i += 1
