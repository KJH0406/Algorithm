import sys     

N = int(sys.stdin.readline())
li = []
for i in range(N):
    num = int(sys.stdin.readline())
    li.append(num)
num_list = sorted(li)
for j in range(N):
    print(num_list[j])