A = input()
B = input()
LCS = [0] * len(A)

for i in range(len(B)):
    cnt = 0
    for j in range(len(A)):
        if cnt < LCS[j]:
            cnt = LCS[j]
        elif B[i] == A[j]:
            LCS[j] = cnt + 1

print(max(LCS))