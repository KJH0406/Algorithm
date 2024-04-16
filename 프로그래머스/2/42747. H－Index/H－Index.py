def solution(citations):
    answer = 0
    
    if len(citations) == 1:
        return citations[0]
    
    # H-Index 탐색을 위해 오름차순 정렬
    citations.sort()

    # 길이 저장
    citations_length = len(citations)
    
    # Index 비교를 위해 배열 길이 맞춤
    citations_idx_count = [0] * (citations[-1] + 1)
    
    for i in citations:
        for j in range(i + 1):
            citations_idx_count[j] += 1
    
    for k in range(citations[-1] - 1, -1, -1):
        if citations_idx_count[k] >= k:
            answer = k
            break
            
    return answer