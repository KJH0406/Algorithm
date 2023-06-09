n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()  

cnt = 0
l = 0
r = n - 1

while l < r:
    if numbers[l] + numbers[r] == x:
        cnt += 1
        l += 1
        r -= 1
    elif numbers[l] + numbers[r] < x:
        l += 1
    else:
        r -= 1

print(cnt)
