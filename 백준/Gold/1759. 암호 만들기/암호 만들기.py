from itertools import combinations

def check(str):
    count = 0
    count += str.count('b')
    count += str.count('c')
    count += str.count('d')
    count += str.count('f')
    count += str.count('g')
    count += str.count('h')
    count += str.count('j')
    count += str.count('k')
    count += str.count('l')
    count += str.count('m')
    count += str.count('n')
    count += str.count('p')
    count += str.count('q')
    count += str.count('r')
    count += str.count('s')
    count += str.count('t')
    count += str.count('v')
    count += str.count('w')
    count += str.count('x')
    count += str.count('y')
    count += str.count('z')
    return count


L, C = map(int, input().split())
password = list(input().split())
result = []
res = []
final_res = []


for i in range(len(password)+1):
  result = result+list(combinations(password, i))

for item in result:
    if len(item) == L:
        item = ''.join(map(str, item))
        res.append(item)
for item in res:
    if 'a' in item or 'e' in item or 'i' in item or 'o' in item or 'u' in item:
        final_password = list(item)
        final_password.sort()
        final_res.append(''.join(map(str, final_password)))

final_res.sort()

for item in final_res:
    if check(item) >= 2:
        print(item)


