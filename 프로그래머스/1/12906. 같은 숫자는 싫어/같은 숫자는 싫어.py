def solution(arr):
    answer = []
    for number in arr:
        if answer:
            if number != answer[-1]:
                answer.append(number)
        else:
            answer.append(number)
    return answer