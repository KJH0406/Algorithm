N = int(input())
switch = [0] + list(map(int, input().split()))
students = int(input())
boy_girl = [list(map(int, input().split())) for _ in range(students)]

for item in boy_girl:
    if item[0] == 1:
        for i in range(item[1], N+1, item[1]):
            switch[i] = 1 - switch[i]
    else:
        i = item[1]
        c = 0
        while i-c >= 1 and i+c <= N and switch[i-c] == switch[i+c]:
            c += 1
        for j in range(i-c+1, i+c):
            switch[j] = 1 - switch[j]

for i in range(1, N+1, 20):
    print(*switch[i:i+20])
