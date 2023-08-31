bracket = list(input())
bl = len(bracket)
cnt = 0
stack = []

for i in range(bl):
    if bracket[i] == '(':
        stack.append('(')
    else:
        if bracket[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop() 
            cnt += 1

print(cnt)
