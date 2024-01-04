S = list(input())
flag = 0
ans = ''
stack = []

while S:
    item = S.pop(0)  # 문자 추출
    if item == '<':  # 괄호 안은 뒤집지 않음.
        if stack:
            while stack:
                ans += stack.pop()
        ans += item  # 여는 괄호 추가
        flag = 1  # 괄호 열음 표시
        while True:
            sub_item = S.pop(0)  # 괄호 열은 후 닫을 때 까지 문자 추출
            if sub_item == '>':  # 닫는 괄호일 때
                ans += sub_item  # 닫는 괄호 추가
                flag = 0  # 괄호 닫음 표시
                break  # 문자 추출 종료
            else:
                ans += sub_item  # 괄호 닫을 때 까지 문자 추출
    # 공백일 때
    elif item == ' ' and stack:
        # 스택에 있는 단어 결과에 더함
        while stack:
            ans += stack.pop()
        ans += ' '
    else:
        stack.append(item)

if stack:
    while stack:
        ans += stack.pop()
print(ans)






