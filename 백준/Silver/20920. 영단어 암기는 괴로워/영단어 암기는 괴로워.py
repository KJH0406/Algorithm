import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    word = input().rstrip()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

temp = []
for key, value in dic.items():
    temp.append((value, key))

temp.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))

flag = temp[0][0]
ans = []
temp_ans = []
for value, key in temp:
    if len(key) >= M:
        if value != flag:
            ans.append(temp_ans)
            flag = value
            temp_ans = []
            temp_ans.append(key)
        else:
            temp_ans.append(key)


if temp_ans:
    ans.append(temp_ans)
for item in ans:
    for item2 in item:
        print(item2)



