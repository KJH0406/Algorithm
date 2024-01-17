N = int(input())


def hanoi(disk, start, goal, sub):
    if disk == 1:
        print(start, goal)
        return
    hanoi(disk - 1, start, sub, goal)
    print(start, goal)
    hanoi(disk - 1, sub, goal, start)


print(2 ** N - 1)
hanoi(N, 1, 3, 2)