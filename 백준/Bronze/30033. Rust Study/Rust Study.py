N = int(input())
S = 0
f = list(map(int, input().split()))
p = list(map(int, input().split()))
for i in range(N):
    if f[i] <= p[i]:
        S +=1
print(S)
