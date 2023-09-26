import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
p = 0
s = 0

while nums:
    if nums:
        p += nums.pop(0)
    else:
        break
    if nums:    
        s += nums.pop()
    else:
        break

print(s, p)