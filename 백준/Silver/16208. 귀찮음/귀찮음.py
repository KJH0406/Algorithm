N = int(input())
arr = list(map(int, input().split()))
arr.sort()
S = sum(arr)
ans  = 0
for i in arr:
    ans += i * (S - i)
    S -= i
print(ans)