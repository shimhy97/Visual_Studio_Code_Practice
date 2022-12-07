

def solution(numbers, target):
    answerList = []
    answer = 0 
    for (n, num) in enumerate(numbers):
        if n == 0 :
            answerList.append(num)
            answerList.append(-num)
        else:
            for i in answerList:
                answerList.append(i+num)
                answerList.append(i-num)
                
    for child in answerList:
        if child == target:
            answer+=1
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
