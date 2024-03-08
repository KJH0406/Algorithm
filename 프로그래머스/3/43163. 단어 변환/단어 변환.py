from collections import deque

def solution(begin, target, words):
    answer = 0
    
    words = [""] + words
    
    visited = [0] * len(words)
    
    queue = deque([(0, begin)])
    
    visited[0] = 1
    
    
    if target not in words:
        return 0
    
    else:
        while queue:
            current_idx, current_word = queue.popleft()
            if current_word == target:
                return visited[current_idx] - 1
            else:
                for i in range(1, len(words)):
                    next_word = words[i]
                    if visited[i] == 0:
                        diff = 0
                        for j in range(len(target)):
                            if current_word[j] != next_word[j]:
                                diff += 1
                        if diff == 1:
                            queue.append((i, next_word))
                            visited[i] = visited[current_idx] + 1

    
    # return answer