N = int(input())
arr = [0] * 1001
post = []
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    post.append((L, H))

post.sort()
max_index = arr.index(max(arr))

s = 0
count = 0
res = 0

for i in range(1, max_index):
    if arr[i] > count:
        count = arr[i]
    res += count
count = 0
for i in range(post[-1][0], max_index-1, -1):
    if arr[i] > count:
        count = arr[i]
    res += count

print(res)
