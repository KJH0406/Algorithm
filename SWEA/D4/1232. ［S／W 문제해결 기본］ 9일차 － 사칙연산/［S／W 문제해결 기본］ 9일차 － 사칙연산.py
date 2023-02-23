# 후위순회
def postorder(node):
    global stack
    if node != 0:
        postorder(tree[node][0])  # 왼쪽 자식
        postorder(tree[node][2])  # 오른쪽 자식
        stack.append(tree[node][1])
 
for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]
    for _ in range(N):
        lst = list(input().split())
        if len(lst) == 2:
            tree[int(lst[0])][1] = int(lst[1])
        elif len(lst) == 3:
            tree[int(lst[0])][1] = lst[1]
            tree[int(lst[0])][0] = int(lst[2])
        elif len(lst) == 4:
            tree[int(lst[0])][1] = lst[1]
            tree[int(lst[0])][0] = int(lst[2])
            tree[int(lst[0])][2] = int(lst[3])
 
    stack = []
    postorder(1)
 
    result = []
    for i in stack:
        if str(i).isdigit():
            result.append(i)
        else:
            second = result.pop()
            first = result.pop()
            if i == '-':
                res = first - second
                result.append(res)
            elif i == '+':
                res = first + second
                result.append(res)
            elif i == '*':
                res = first * second
                result.append(res)
            else:
                res = first / second
                result.append(res)
 
    print(f'#{tc} {int(result[0])}')
