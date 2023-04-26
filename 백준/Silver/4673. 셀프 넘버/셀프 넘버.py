numbers = list(range(1, 10001))
self_numbers = []
temp = []
for i in range(1, 10001):
    s = 0
    s += i
    for j in str(i):
        s += int(j)
    temp.append(s)

for item in numbers:
    if item not in temp:
        self_numbers.append(item)
for item in self_numbers:
    print(item)