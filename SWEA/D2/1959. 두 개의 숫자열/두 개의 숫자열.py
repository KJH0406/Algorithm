T = int(input())
for tc in range(1, T+1):
    li_len = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) > len(B):
        A, B = B, A
    ans = []
    for i in range(len(B)-len(A)+1):
        s = 0
        for j in range(len(A)):
            s += A[j] * B[j+i]
        ans.append(s)
    print(f'#{tc} {max(ans)}')
