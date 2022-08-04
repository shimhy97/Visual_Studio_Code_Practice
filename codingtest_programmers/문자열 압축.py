import math

def solution(s):

    length = []
    if len(s) == 1:
        answer = 1
        return answer

    for i in range(1,len(s)) :
        parsedWordList = []
        iter_ = 0
        iterEachWord = 1
        numOfWord = math.ceil(len(s)/i)   ## < 치명적인 오류
        
        
        ansString = ""  # 초기 배열 지정
        
        
        ### 문자열 일정 길이로 나누기
        for iter_ in range(numOfWord): 
            
            if iter_ == 0:
                parsedWordList.append(s[0:i])
                iter_ += 1
                continue
                
            currentIndex = i*iter_
            afterIndex = i*(iter_+1)
            
            if afterIndex <= len(s) :  # 범위 내에 있다면
                indexedWord = s[currentIndex:afterIndex]
                iter_ += 1
            elif afterIndex > len(s) :     # 끝부분이 남아서 범위를 초과한다면
                indexedWord = s[currentIndex:]

            parsedW ordList.append(indexedWord)

        if indexedWord != "":
            parsedWordList.append("") 

        # 압축 횟수 명시 알고리즘.
        temp = parsedWordList[0]
        for iter_ in range(0,len(parsedWordList)-1):
            
            # if iter_ == len(parsedWordList):

            #     break

            currentWord = parsedWordList[iter_]
            afterWord = parsedWordList[iter_+1]

            if currentWord == afterWord:
                iterEachWord +=1
                
            elif currentWord != afterWord:

                ansString = ansString + str(iterEachWord) + temp if iterEachWord != 1 else ansString + temp
                temp = afterWord
                iterEachWord = 1

        length.append(len(ansString))

        # print(f"{i}일때 해답 : {len(ansString)},{ansString}")
    ## end for    
    answer = min(length)
    
    return answer
       
        
solution("abcabcdede")