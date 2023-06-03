a, b = map(int, input().split())
m = int(input())
s = a + b
if s >= (2 * m):
    print(s - (2 * m))
else:
    print(s)