T = int(input())

for _ in range(T):
    res = []
    temp = []
    char = list(input())
    for item in char:
        if item == '<' and res:
            temp.append(res.pop())
        elif item == '>' and temp:
            res.append((temp.pop()))
        elif item == '-' and res:
            res.pop()
        elif item not in ('<', '>', '-'):
            res.append(item)

    while temp:
        res.append(temp.pop())
    print(''.join(res))

