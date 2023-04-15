a = []
b = []
for _ in range(4):
    a.append(int(input()))
for _ in range(2):
    b.append(int(input()))

s = 0
a.sort(reverse=True)
s += max(b)
s += sum(a[:3])
print(s)
