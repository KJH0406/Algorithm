def solution(numbers, target):
    answer = 0
    
    memo = {}  # 메모이제이션을 위한 딕셔너리 (key: (index, current_sum), value: 방법의 수)

    def dfs(index, current_sum):
        # 탐색이 끝났을 때, current_sum이 target과 일치하는지 확인
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # 이미 계산된 경우, 저장된 결과 반환
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]
        
        # 현재 숫자를 더하거나 빼는 경우를 모두 탐색
        count = dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
        
        # 결과 저장 후 반환
        memo[(index, current_sum)] = count
        return count

    answer = dfs(0, 0)
    
    return answer
