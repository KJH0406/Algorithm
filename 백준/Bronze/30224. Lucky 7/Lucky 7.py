N = int(input())
t = str(N)

if '7' not in t and N % 7 != 0:
    print(0)
elif '7' not in t and N % 7 == 0:
    print(1)
elif '7' in t and N % 7 != 0:
    print(2)
elif '7' in t and N % 7 == 0:
    print(3)
    