S = input()
S_li = len(S)

for i in range(S_li):
    if S[i:] == S[i:][::-1]:
        print(S_li + i)
        break