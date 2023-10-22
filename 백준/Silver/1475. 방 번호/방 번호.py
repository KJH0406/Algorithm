N = input()
res = [0] * 10
for i in range(len(N)):
    k = int(N[i])
    if k == 6 or k == 9:
        if res[6] <= res[9]:
            res[6] += 1
        else:
            res[9] += 1
    else:
        res[k] += 1

print(max(res))