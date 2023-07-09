from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())

heap = []

for _ in range(N):
    t = int(input())
    if heap and t == 0:
        res = heappop(heap)
        print(res[1])
    elif t == 0:
        print(0)
    else:
        heappush(heap, [abs(t), t])


