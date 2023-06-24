def dfs(n):
    global ans
    if n == N:  # 종료조건 : N까지 진행한 경우의 경우의 수
        ans += 1
        return  # 종료
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:  # 열, 대각선에 퀸이 없는 경우
            v1[j] = v2[n+j] = v3[n-j] = 1  # 퀸 놓음.
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0  # 실행 후 다음 백트래킹 위해서 초기화


N = int(input())

ans = 0
v1 = [0] * N  # 열 체크
v2 = [0] * (N * 2)  # 대각선 체크
v3 = [0] * (N * 2)  # 대각선 체크

dfs(0)  # 백트래킹
print(ans)  # 정답 출력