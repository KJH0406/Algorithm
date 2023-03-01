square = [list(map(int, input().split())) for _ in range(4)]
x1 = y1 = p1 = q1 = x2 = y2 = p2 = q2 = 0

for item in square:
    x1, y1 = item[0], item[1]
    p1, q1 = item[2], item[3]
    x2, y2 = item[4], item[5]
    p2, q2 = item[6], item[7]

    if (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2):
        print('c')
    elif (q1 < y2) or (q2 < y1) or (p1 < x2) or (p2 < x1):
        print('d')
    elif q1 == y2 or q2 == y1 or x1 == p2 or p1 == x2:
        print('b')
    else:
        print('a')


