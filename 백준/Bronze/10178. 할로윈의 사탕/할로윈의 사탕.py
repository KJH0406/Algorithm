n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    res_a = a // b
    res_b = a % b
    print(f'You get {res_a} piece(s) and your dad gets {res_b} piece(s).')