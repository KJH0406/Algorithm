N, M = map(int, input().split())

dic = {}

for i in range(1, N + 1):
    item = input()
    dic[item] = i
    dic[str(i)] = item

for j in range(1, M+1):
    print(dic[input()])
