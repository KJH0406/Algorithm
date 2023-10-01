s = input()
c = 0
sl = len(s)
for i in range(sl-1):
    if s[i] != s[i+1]:
        c += 1
c += 1
print(c // 2)