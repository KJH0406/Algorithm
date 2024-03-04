from collections import deque

def solution(numbers, target):
    answer = 0
    current_sums = deque([0])  # 초기 합계를 0으로 설정하여 시작

		# 기존 숫자 배열 순회
    for number in numbers:
        next_sums = deque()  	# 탐색할 덱 생성
        while current_sums :
            current_sum = current_sums.popleft()
            next_sums.append(current_sum + number)  # 양수(+) 값 반영
            next_sums.append(current_sum - number)  # 음수(+) 값 반영
				
        current_sums = next_sums  # 기존 합계에 반영

    answer = current_sums.count(target)  # 타겟 수 카운트

    return answer