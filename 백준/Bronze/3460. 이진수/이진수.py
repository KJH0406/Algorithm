
T = int(input())
for _ in range(T):
    a = int(input())
    b = bin(a)[2:]
    for i in range(len(b)):
        if b[-i-1] == '1' and i != len(b)-1:
            print(i, end=' ')
        elif b[-i-1] == '1' and i == len(b)-1:
            print(i)