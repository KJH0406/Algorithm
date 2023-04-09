cnt = 1
while True:
    li = list(map(int, input().split()))
    if len(li) == 1 and li[0] == 0:
        break
    else:
        print(f'Case {cnt}: Sorting... done!')
    cnt += 1