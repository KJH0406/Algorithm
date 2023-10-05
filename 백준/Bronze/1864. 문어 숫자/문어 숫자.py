dic = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    A = input()
    AL = len(A)
    if A == '#':
        break
    ans = 0
    for i in range(AL):
        ans += dic[A[i]] * 8 ** (len(A) - i - 1)
    print(ans)