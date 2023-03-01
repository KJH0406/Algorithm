K = int(input())
length = [list(map(int, input().split())) for _ in range(6)]
wide = []
height = []
res = []
for item in length:
    res.append(item[1])
    if item[0] == 1 or item[0] == 2:
        wide.append(item[1])
    else:
        height.append(item[1])
max_wide = max(wide)
max_height = max(height)

f_wide = f_height = 0
if res.index(max_wide) == len(res) - 1:
    f_wide = abs(res[(res.index(max_height) - 1)] - res[(res.index(max_height) + 1)])
    f_height = abs(res[(res.index(max_wide) - 1)] - res[0])
    
elif res.index(max_height) == len(res) - 1:
    f_wide = abs(res[(res.index(max_height) - 1)] - res[0])
    f_height = abs(res[(res.index(max_wide) - 1)] - res[(res.index(max_wide) + 1)])
else:
    f_wide = abs(res[(res.index(max_height) - 1)] - res[(res.index(max_height) + 1)])
    f_height = abs(res[(res.index(max_wide) - 1)] - res[(res.index(max_wide) + 1)])
print(K * max_wide * max_height - K * f_wide * f_height)


