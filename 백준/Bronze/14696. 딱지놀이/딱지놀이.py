N = int(input())
for _ in range(N):
    picture_A = list(map(int, input().split()))
    picture_B = list(map(int, input().split()))
    len_A = picture_A.pop(0)
    len_B = picture_B.pop(0)
    if picture_A.count(4) > picture_B.count(4):
        print('A')
    elif picture_A.count(4) < picture_B.count(4):
        print('B')
    elif picture_A.count(3) > picture_B.count(3):
        print('A')
    elif picture_A.count(3) < picture_B.count(3):
        print('B')
    elif picture_A.count(2) > picture_B.count(2):
        print('A')
    elif picture_A.count(2) < picture_B.count(2):
        print('B')
    elif picture_A.count(1) > picture_B.count(1):
        print('A')
    elif picture_A.count(1) < picture_B.count(1):
        print('B')
    else:
        print('D')


