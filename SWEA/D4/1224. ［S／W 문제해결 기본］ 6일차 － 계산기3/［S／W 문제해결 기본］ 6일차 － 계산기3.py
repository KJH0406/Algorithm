for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    stack = []
    res = []
    for item in arr:
        if item.isdigit():
            res.append(item)
        else:
            if not stack:
                stack.append(item)
            else:
                if item == ')':
                    while stack and stack[-1] != '(':
                        res.append(stack.pop())
                    stack.pop()
                else:
                    while stack and icp[item] <= isp[stack[-1]]:
                        res.append(stack.pop())
                    stack.append(item)
    while stack:
        res.append(stack.pop())

    for item in res:
        if item.isdigit():
            stack.append(int(item))
        else:
            if stack and item == '+':
                stack.append(stack.pop() + stack.pop())
            elif stack and item == '*':
                stack.append(stack.pop() * stack.pop())

    print(f'#{tc} {stack.pop()}')





