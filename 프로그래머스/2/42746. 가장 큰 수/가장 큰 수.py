def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 두 문자열을 연결했을 때 더 큰 순서로 정렬
    # 여기서 포인트 : 비교를 위해 일정한 길이의 문자열을 생성
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 문자열을 합쳐서 결과 반환
    answer = ''.join(str_numbers)
    
    # 모든 숫자가 0인 경우 '0'을 반환
    return answer if int(answer) != 0 else '0'
