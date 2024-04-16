def solution(citations):
    # 정렬
    citations.sort()
    
    # H-Index 계산
    n = len(citations)
    
    for i in range(n):
        # citations[i]는 인용 횟수
        # (n - i)는 citations[i] 이상 인용된 논문 수
        if citations[i] >= (n - i):
            return n - i
    
    return 0
