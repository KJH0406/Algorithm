from collections import deque

N = int(input())
li = deque()
record = []
num = []

for _ in range(N):
    push = input().split()
    num.append(push)

for item in num:
    if len(item) == 2:
        record.append(item[0])
        if item[0] == '1':
            li.append(item[1])
        else:
            li.appendleft(item[1])
    else:
        if len(record) != 0:
            check = record.pop()
            if li and check == '1':
                li.pop()
            elif li and check == '2':
                li.popleft()

if li:
    print(''.join(li))
else:
    print(0)