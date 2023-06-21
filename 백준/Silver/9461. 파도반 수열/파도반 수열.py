def dp(k):
    side = [0, 1, 1, 1, 2, 2]
    if k < 6:
        return side[k]
    else:
        for i in range(6, k + 1):
            side.append(side[i-1] + side[i-5])
        return side[k]


n = int(input())

for _ in range(n):
    k = int(input())
    print(dp(k))