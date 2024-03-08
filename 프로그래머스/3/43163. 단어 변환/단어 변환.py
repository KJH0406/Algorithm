from collections import deque

def solution(begin, target, words):
    answer = 0
    
    word_length = target  # 단어 길이
    
    visited = [0] * (len(words) + 1)  # 변환 횟수 저장할 배열 생성
    
    queue = deque([(0, begin)])  # 시작 단어 설정
    
    visited[0] = 1  # 시작 단어 방문 표시
    
    
    # 만약 타겟으로 하는 단어가 단어 배열에 없다면 0을 반환
    if target not in words:
        return 0
    
    else:
        while queue:
            current_idx, current_word = queue.popleft()
            
            # 타겟 단어로 변환이 완료되었을 경우 변환 횟수 반환
            if current_word == target:
                return visited[current_idx] - 1
            else:
                
                # 단어 비교
                for i in range(len(words)):
                    next_word = words[i]
                    next_idx = i + 1
                    if visited[next_idx] == 0:
                        diff = 0
                        for j in range(len(target)):
                            if current_word[j] != next_word[j]:
                                diff += 1
                            if diff > 1:
                                break
                        # 한 번에 한개의 알파벳만 바꿀 수 있음
                        if diff == 1:
                            queue.append((next_idx, next_word))
                            visited[next_idx] = visited[current_idx] + 1

    