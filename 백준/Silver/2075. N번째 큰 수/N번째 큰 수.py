import heapq
N = int(input())
heap = []

for _ in range(N):
    numbers = list(map(int, input().split()))
    if not heap: # 첫 리스트는 기준값으로 다 넣어줌
        for item in numbers:
            heapq.heappush(heap, item)
    else:
        for item in numbers:  # 이제 두번째줄부터 원소 순회
            if heap[0] < item:  # 만약 힙의 가장 작은 값보다 item원소가 더 크면
                heapq.heappush(heap, item)  # 힙에 넣고
                heapq.heappop(heap)  # 힙에서 가장 작은 수를 뺌

print(heap[0])  # 가장 큰 값들중 가장 작은 값이 곧 N번째 큰수임 ( 처음 형성할때부터 길이가 N인 힙이 구성되었으므로 )