N = int(input())
C = 1
for i in range(11, N+1):
    C *= i
C *= 6
print(C)