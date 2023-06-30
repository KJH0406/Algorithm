from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
       try:
            print(heappop(heap))
       except:
            print(0)
    else:
        heappush(heap, num)


