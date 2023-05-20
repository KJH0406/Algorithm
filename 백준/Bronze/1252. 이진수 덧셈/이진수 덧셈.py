a, b = input().split()
a = '0b' + a
b = '0b' + b
ab = int(a, 2) + int(b, 2)
print(bin(ab)[2:])