# 연속한 여러 문자를 하나로 줄이기

def solution(people,limit):
    answer = 0
    people.sort()
    while people:
        if len(people) == 1:
            answer += 1
            break
        if people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop()
            answer += 1
        else:
            people.pop()
            answer += 1
    return answer