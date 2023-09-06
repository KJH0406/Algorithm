a = []
b = []
for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for j in range(3):
    if a.count(a[j]) == 1:
        x = a[j]
    if b.count(b[j]) == 1:
        y = b[j]

print(x, y)