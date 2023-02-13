import sys

N = int(sys.stdin.readline().rstrip())
students = [sys.stdin.readline().rstrip().split() for _ in range(N)]

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in students:
    print(name[0])
