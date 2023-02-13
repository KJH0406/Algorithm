def lay_down(li, N):
    count_li = []
    for item in li:
        count = 0
        for i in range(N):
            if item[i] == '.':
                count += 1
            else:
                count_li.append(count)
                count = 0
        count_li.append(count)
    return count_li

N = int(input())
column = []
res = [list(input()) for _ in range(N)]
lay_count = []

for i in range(N):
    box = []
    for j in range(N):
        box.append(res[j][i])
    column.append(box)

res_count = lay_down(res, N)
column_count = lay_down(column, N)
res_c = 0
col_c = 0

for i in res_count:
    if i >= 2:
        res_c += 1
for i in column_count:
    if i >= 2:
        col_c += 1

print(res_c, col_c)
