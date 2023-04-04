N = int(input())
number = [int(input()) for _ in range(N)]
stack = []
res = []  # pop한 숫자 넣기
ans = []  # 기호 넣기
final = 1
cur = 1

for item in number:
    if stack and stack[-1] == item:
        res.append(stack.pop())
        ans.append('-')
    elif stack and stack[-1] > item:
        print('NO')
        final = 0
        break
    else:
        while cur <= item:
            stack.append(cur)
            ans.append('+')
            cur += 1
        res.append(stack.pop())
        ans.append('-')


if final:
    for result in ans:
        print(result)