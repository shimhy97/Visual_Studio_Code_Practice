'''N으로 표현
문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항

N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
'''
def solution(N, number):
    # 허뎝님의 수정 피드백 -> 테스트 케이스가 바뀌면서 예외 사항을 추가해야 함.
    if N == number:
        return 1
        
    # 1. [ SET x 8 ] 초기화
    s = [ set() for x in range(8) ] 

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )

    # 3. n 일반화
    #   { 
    #       "n" * i U 
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set, 
    #    } 
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer