def check(chess):
    count = 0
    res = []
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            if chess[i][j] != 'W':
                count += 1
        for j in range(1, 8, 2):
            if chess[i][j] != 'B':
                count += 1
    for i in range(1, 8, 2):
        for j in range(0, 8, 2):
            if chess[i][j] != 'B':
                count += 1
        for j in range(1, 8, 2):
            if chess[i][j] != 'W':
                count += 1

    res.append(count)
    count = 0

    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            if chess[i][j] != 'B':
                count += 1
        for j in range(1, 8, 2):
            if chess[i][j] != 'W':
                count += 1
    for i in range(1, 8, 2):
        for j in range(0, 8, 2):
            if chess[i][j] != 'W':
                count += 1
        for j in range(1, 8, 2):
            if chess[i][j] != 'B':
                count += 1

    res.append(count)

    return min(res)

def generate_8x8_arrays(arr):
    arrays = []
    for i in range(len(arr)-7):
        for j in range(len(arr[0])-7):
            new_arr = [row[j:j+8] for row in arr[i:i+8]]
            arrays.append(new_arr)
    return arrays


N, M = map(int, input().split())

li = [list(input()) for _ in range(N)]

cnt = []

final = generate_8x8_arrays(li)


for item in final:
    cnt.append(check(item))
print(min(cnt))




