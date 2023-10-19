a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = False

for i in range(len(a)):
    if sum(a[:i+1]) > sum(b[:i]):
        res = True
if res and sum(a) < sum(b):
    print('Yes')
else:
    print('No')