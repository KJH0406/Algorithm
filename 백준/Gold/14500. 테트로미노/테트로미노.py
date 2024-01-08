n, m = map(int, input().split())  # n: 세로 , m: 가로
arr = [list(map(int, input().split())) for _ in range(n)]

max_value = 0

# 4개 가로 - 가로 판단
if m - 4 >= 0:
    for i in range(n):
        for j in range(m - 3):
            max_value = max(max_value, sum(arr[i][j:j + 4]))

# 4개 가로 - 세로 판단
if n - 4 >= 0:
    for j in range(m):
        for i in range(n - 3):
            temp_value = 0
            for k in range(4):
                temp_value += arr[i + k][j]
            max_value = max(max_value, temp_value)

# 정사각형
if m - 2 >= 0 and n - 2 >= 0:
    for i in range(n - 1):
        for j in range(m - 1):
            temp_value2 = arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            max_value = max(max_value, temp_value2)

# 6개 가로
if m - 3 >= 0 and n - 2 >= 0:
    for i in range(n - 1):
        for j in range(m - 2):
            cases = []
            cases.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j])
            cases.append(arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2])
            cases.append(arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1])
            cases.append(arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2])
            cases.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1])
            cases.append(arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2])
            cases.append(arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2])
            cases.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2])
            max_value = max(max_value, max(cases))

# 6개 세로
if m - 2 >= 0 and n - 3 >= 0:
    for i in range(n - 2):
        for j in range(m - 1):
            cases = []
            cases.append(arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1])
            cases.append(arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1])
            cases.append(arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1])
            cases.append(arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j])
            cases.append(arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j])
            cases.append(arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1])
            cases.append(arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1])
            cases.append(arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 2][j])
            max_value = max(max_value, max(cases))
print(max_value)

