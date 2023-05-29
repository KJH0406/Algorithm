n = int(input()) #총합    
s = 0 
cnt = 0 # 1씩 증가함

while True:
    cnt += 1
    s += cnt
    if s > n:
        break

print(cnt - 1)