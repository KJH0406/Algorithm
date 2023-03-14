cro = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
li = input()
alpha = list(li)
check = ['@'] + alpha

cnt = 0

if li.count('dz=') > 0:
    for i in range(1, len(check)-1):
        string = check[i] + check[i+1]
        if string in cro and string != 'z=':
            cnt += 1
        elif string == 'z=' and check[i-1] == 'd':
            cnt += 2
        elif string == 'z=':
            cnt += 1
else:
    for i in range(len(alpha)-1):
        string = alpha[i] + alpha[i+1]
        if string in cro:
            cnt += 1
print(len(alpha)-cnt)











