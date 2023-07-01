
A, B = map(int, input().split())

queue = []
queue.append((A, A * 2, int(str(A) + '1')))
cnt = 1
flag = 0
while queue:
    p = queue.pop(0)
    if B in p:
        flag = 1
        break
    else:
        temp = set()
        for item in p:
            if 0 < item * 2 <= B:
                temp.add(item * 2)
            if 0 < int(str(item) + '1') <= B:
                temp.add(int(str(item) + '1'))
        if temp:
            queue.append(temp)
    cnt += 1

if flag:
    print(cnt + 1)
else:
    print(-1)


