import sys
from operator import itemgetter

students = []
N = int(input())
for i in range(N):
    students.append(sys.stdin.readline().split())

students = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in students:
    print(name[0])
