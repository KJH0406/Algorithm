def max_value(li):
    maxV = 0
    for item in li:
        if maxV < item:
            maxV = item
    return maxV


def min_value(li):
    minV = li[0]
    for item in li:
        if minV > item:
            minV = item
    return minV


for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    for _ in range(dump):
        if max_value(box) - min_value(box) <= 1:
            break
        else:
            box[box.index(max_value(box))] -= 1
            box[box.index(min_value(box))] += 1
    print(f'#{tc} {max_value(box) - min_value(box)}')