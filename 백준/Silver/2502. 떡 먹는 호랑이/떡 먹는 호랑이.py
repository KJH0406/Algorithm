def check(D, a, b):
    arr = [0] * (D+1)
    arr[1] = a
    arr[2] = b
    for i in range(3, D+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[D]

D, K = map(int, input().split())
arr = [0] * (D+1)
arr[D] = K
stop = 0

for a in range(1, K):
    for b in range(1, K):
        if check(D, a, b) == K:
            print(a)
            print(b)
            stop += 1
            break
    if stop != 0:
        break
