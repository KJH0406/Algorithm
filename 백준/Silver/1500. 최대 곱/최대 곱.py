S, K = map(int, input().split())

share = S // K
remain = S % K
numbers = [share] * K

for i in range(remain):
    numbers[i] += 1

res = 1
for item in numbers:
    res *= item

print(res)






