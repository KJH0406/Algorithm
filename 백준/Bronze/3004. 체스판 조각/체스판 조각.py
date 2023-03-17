def slicing(N):
    arr = [0] * 101
    arr[1] = 2
    arr[2] = 4
    if arr[N] == 0:
        for i in range(3, N+1):
            if i % 2 == 0:
                arr[i] = (i//2 + 1) ** 2
            else:
                arr[i] = arr[i-1] * 2 - arr[i-2]
        return arr[N]
    else:
        return arr[N]


N = int(input())

print(slicing(N))
