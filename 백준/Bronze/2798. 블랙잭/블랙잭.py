N, M = map(int, input().split())
numbers = list(map(int, input().split()))
res = []
for i in range(len(numbers)):
    num = numbers.pop(i)
    for j in range(len(numbers)-1, -1, -1):
        for k in range(0, j):
            if num + numbers[k] + numbers[j] <= M:
                res.append(num + numbers[k] + numbers[j])
    numbers.append(num)
print(max(res))