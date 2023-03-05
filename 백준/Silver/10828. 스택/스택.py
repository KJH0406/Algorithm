N = int(input())
p = []
stack = []
for _ in range(N):
    p.append(input().split())
for item in p:
    if len(item) == 1:
        if item[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif item[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif item[0] == 'size':
            print(len(stack))
        elif item[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
    else:
        stack.append(item[1])