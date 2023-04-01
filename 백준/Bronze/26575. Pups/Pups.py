a = int(input())
for _ in range(a):
    b,c,d = map(float, input().split())
    print(f'${b*c*d:.2f}')