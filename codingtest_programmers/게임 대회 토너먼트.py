import math

def solution(n,a,b):
    
    # 재귀함수의 첫 부분. 끝내는 조건
    
    i = 0
    checkn = n
    while checkn != 1 :
        checkn = checkn // 2
        i += 1
    
    # 재귀함수의 동작 부분.

    rangeBefore = range (1,n//2 + 1)
    rangeAfter = range(n//2 + 1 , n + 1)
    
    # a,b 가 다른 그룹이라면? 연산 끝내기
    
    if (a in rangeBefore and b in rangeAfter) or (a in rangeAfter  and b in rangeBefore) :
        print("다른 그룹. 만날 수 있습니다.")
        answer = i
        print(f" 만나려면{answer}번 경기해야 합니다.")
        return answer 

    # a,b 가 같은 그룹이라면 ? 한번 더 나눠야 함.
    elif (a in rangeBefore and b in rangeBefore) :
        print("Same Group, 연산 추가 수행")
        n = n//2
        solution(n,a,b)    

    elif (a in rangeAfter  and b in rangeAfter) :
        print("Same Group, 연산 추가 수행")
        a = int(math.ceil(a/2))
        b = int(math.ceil(b/2)) if a != b else int(math.ceil(b/2)) + 1
        n = n//2
        solution(n,a,b)    



solution(8,3,7)
solution(32,31,32)