def backtrack(n, s, cnt):  # cnt => 원소 포함한 개수
    global ans
    if n == N:
        if s == K and cnt > 0:
            ans += 1
        return

    backtrack(n+1, s + A_list[n], cnt + 1)
    backtrack(n+1, s, cnt)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    ans = 0
    backtrack(0, 0, 0)
    print(f'#{tc} {ans}')

