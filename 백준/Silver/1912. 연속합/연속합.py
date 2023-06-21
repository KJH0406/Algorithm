n = int(input())
numbers = list(map(int, input().split()))
res = numbers[0]
ans = numbers[0]
for i in range(1, n):
    temp = [res + numbers[i], numbers[i]]
    res = max(temp)
    if ans < res:
        ans = res
print(ans)

