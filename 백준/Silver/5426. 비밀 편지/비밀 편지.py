N = int(input())

for _ in range(N):
    li = [0] + list(input())
    K = int(len(li) ** (1/2))
    ans = []
    for i in range(K, 0, -1):
        ans.append(li[i])
        temp = i
        for j in range(K-1):
            temp += K
            ans.append(li[temp])
    print(''.join(map(str, ans)))