def solution(s):
    flag = 0

    for bracket in s:
        if bracket == '(':
            flag += 1
        else:
            if flag == 0:
                return False  # 여는 괄호 없이 닫는 괄호가 나오면 바로 False 반환
            flag -= 1

    return flag == 0  # 모든 검사 후 괄호의 수가 맞지 않으면 False 반환