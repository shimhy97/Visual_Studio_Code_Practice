# 1,2,3 더하기

# 정수를 1,2,3의 합으로 나타내는 방법은 총 7가지가 있다. 

memory = {}

def answer(N):
    
    if N == 1:
        return 1
    elif N == 2 :
        return 2
    elif N == 3 :
        return 4
    else :
        return answer(N-1) + answer(N-2) + answer(N-3)
        
N = int(input())
print(answer(N))