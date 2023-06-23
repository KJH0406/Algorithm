N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(triangle[0][0])
else:
    for i in range(1, N):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    print(max(triangle[-1]))