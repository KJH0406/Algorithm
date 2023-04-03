T = int(input())
numbers = list(map(int, input().split()))

J = []
H = []

for i in range(T-1):
    for j in range(i + 1, T):
        if abs(numbers[i] - numbers[j]) % 2 == 0:
            J.append(abs(numbers[i] - numbers[j]))
        else:
            H.append(abs(numbers[i] - numbers[j]))

if len(J) != 0 and len(H) != 0:
    print(f'{min(J)} {min(H)}')
elif len(J) == 0:
    print(f'-1 {min(H)}')
elif len(H) == 0:
    print(f'{min(J)} -1')
