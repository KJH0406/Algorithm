students = []
N = int(input())
for _ in range(N):
    name, a, b, c = input().split()
    students.append((int(a), int(b), int(c), name))

students.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for a, b, c, name in students:
    print(name)
