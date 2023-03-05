T = int(input())

for _ in range(T):
    stack = []
    li = list(input())
    for item in li:
        if item == '(':
            stack.append(item)
        else:
            if not stack:
                stack.append(item)
            elif stack[-1] == '(':
                stack.pop()
    if stack:
        print('NO')
    else:
        print('YES')
