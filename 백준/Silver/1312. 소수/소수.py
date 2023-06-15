A, B, N = map(int, input().split())

q = A // B
r = A % B

# 나머지에 10을 곱하고 몫을 구하는 과정 반복
for _ in range(N):
    r *= 10
    q = r // B
    r %= B

print(q)