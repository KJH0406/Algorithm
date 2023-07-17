H1, M2, S3 = map(int, input().split())
D = int(input()) 

S3 += D % 60
D = D // 60
if S3 >= 60:
    S3 -= 60
    M2 += 1

M2 += D % 60
D = D // 60
if M2 >= 60:
    M2 -= 60
    H1 += 1

H1 += D % 24
if H1 >= 24:
    H1 -= 24

print(H1,M2,S3)