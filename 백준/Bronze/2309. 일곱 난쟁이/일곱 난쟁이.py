li = []
li2 = []
for _ in range(9):
    li.append(int(input()))

for i in range(len(li)-1, -1, -1):
    for j in range(0, i):
        li2.append((li[i], li[j]))

for a, b in li2:
    li.remove(a)
    li.remove(b)
    if sum(li) == 100:
        li.sort()
        for item in li:
            print(item)
        break
    else:
        li.append(a)
        li.append(b)