def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    i=0
    answer=""
    while i <= len(participant):
        try:
            if participant[i] == completion[i]:
                i = i+1
                continue
            else: 
                answer = participant[i]
                break
        except:
            answer =  participant[i]
            break
    return answer

a = solution(["leo", "kiki", "eden"],["eden", "kiki"])
print(a)