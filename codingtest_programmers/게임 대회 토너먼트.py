import math

def solution(n,a,b):
    
    # 재귀함수의 첫 부분. 끝내는 조건

    a = math.ceil(a/2)
    b = math.ceil(b/2)

    # 재귀함수의 동작 부분.
    
    if a != b :
        m = n / 2
        solution (m,a,b)


    if a == b :
        checkn = n / m
        i = 0
        while checkn != 1:
            checkn = checkn /2 
            i+=1
        answer = i
        print(f"{n}명일때{a}와{b}가 만나려면 {answer}번 경기해야 함")
        return answer


solution(8,3,7)
solution(32,30,32)