N, L = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
for item in li:
    if item > L:
        break
    else:
        L += 1
print(L)
    

