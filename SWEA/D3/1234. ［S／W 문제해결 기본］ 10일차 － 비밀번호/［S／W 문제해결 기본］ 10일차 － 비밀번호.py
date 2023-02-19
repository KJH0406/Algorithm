for tc in range(1, 11):
    N, num_list = input().split()
    stack = []
    for item in num_list:
        if not stack:
            stack.append(item)
        else:
            if stack[-1] != item:
                stack.append(item)
            else:
                stack.pop()
    print(f'#{tc}', ''.join(stack))
    
