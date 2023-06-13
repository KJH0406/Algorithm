import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    ans = input().strip()
    if ans == 'all':
        S = set(list(range(1, 21)))
    elif ans == 'empty':
        S = set()
    else:
        cmd, x = ans.split()
        x = int(x)
        if cmd == 'add' and x not in S:
            S.add(x)
        elif S and cmd == 'remove' and x in S:
            S.remove(x)
        elif cmd =='check':
            if S and x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if S and x in S:
                S.remove(x)
            else:
                S.add(x)


