import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
set_numbers = set(numbers)
set_list = list(set_numbers)
set_list.sort()
for item in numbers:
    cnt = 0
    left = 0
    right = len(set_list)-1
    while left <= right:
        mid = (left + right) // 2
        if set_list[mid] < item:
            left = mid + 1
        elif set_list[mid] > item:
            right = mid - 1
        else:
            cnt += mid
            break
    print(cnt, end=' ')