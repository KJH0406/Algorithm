import sys
input = sys.stdin.readline

N = int(input())
FR = 1 # 곱셈 받을 기본 값

# 매번 수를 곱해나가면서 가장 뒤에 있는 0을 없애줘야함.
for i in range(2, N + 1):
    #i를 통해 곱해줌.
    FR *= i
    while True:
        # 수가 너무 길어지지않게 뒤가 0이면 바로 지워줌.
        # 뒤 숫자 계속 확인하기 위해 문자열 변환
        if str(FR)[-1] == "0":
            FR //= 10 # 0지우기
        else:
            break
    FR %= 100000000000000000

print(str(FR)[-5:]) # 뒤에서 5자리 출력