a, b = map(int, input().split())
a_count = 1
b_count = 1
c_count = 1
for i in range(1, a + 1):
    a_count = a_count * i

for i in range(1, b + 1):
    b_count = b_count * i

for i in range(1, a - b + 1):
    c_count = c_count * i

print(a_count // (b_count * c_count))


