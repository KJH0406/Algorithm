wide, height = map(int, input().split())
N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
si, sj = map(int, input().split())
count = 0
if si == 1:  # 북쪽
    for item in arr:
        x = item[0]
        y = item[1]
        if x == 1:
           count += abs(sj - y)
        elif x == 2:
            L_path = sj + height + y
            R_path = wide - sj + height + wide - y
            if L_path > R_path:
                count += R_path
            else:
                count += L_path
        elif x == 3:
            count += sj + y
        else:
            count += wide - sj + y

elif si == 2:  # 남쪽
    for item in arr:
        x = item[0]
        y = item[1]
        if x == 1:
            L_path = sj + height + y
            R_path = wide - sj + height + wide - y
            if L_path > R_path:
                count += R_path
            else:
                count += L_path
        elif x == 2:
            count += abs(sj - y)
        elif x == 3:
            count += sj + height - y
        else:
            count += wide - sj + height - y
elif si == 3:  # 서쪽
    for item in arr:
        x = item[0]
        y = item[1]
        if x == 1:
            count += sj + y
        elif x == 2:
            count += height - sj + y
        elif x == 3:
            count += abs(sj - y)
        else:
            L_path = sj + wide + y
            R_path = height - sj + wide + height - y
            if L_path > R_path:
                count += R_path
            else:
                count += L_path
else:  # 동쪽
    for item in arr:
        x = item[0]
        y = item[1]
        if x == 1:
            count += sj + wide - y
        elif x == 2:
            count += height - sj + wide - y
        elif x == 3:
            L_path = sj + wide + y
            R_path = height - sj + wide + height - y
            if L_path > R_path:
                count += R_path
            else:
                count += L_path
        else:
            count += abs(sj - y)
print(count)