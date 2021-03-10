# 참고문헌 : https://wikidocs.net/18



def ask():

    questions=[]
    answers=[]
    result={}

    while True:
        a = input("질문을 입력해주세요 : ")
        if a == "q":
            break
        else:
            questions.append(a)
            print(questions)
        
    while len(questions)!=len(answers):
        for i in questions:
            print(i)
            b = input(">>답변을 입력해주세요 : ")
            answers.append(b)
    result.update(zip(questions,answers))
    print("결과 : ",result)

ask()