# ------기본값

# def profile (name, age, main_language):
#     print ("이름 = {0}, 나이 = {1} , 주 언어 = {2}".format(name,age,main_language))
#     return name , age , main_language


# profile("유재석",40,"한국어")

# 근데 나이랑 언어가 계속 고정이면?


# def profile (name, age= 20, main_language= "한국어"):
#     print ("이름 = {0}, 나이 = {1} , 주 언어 = {2}".format(name,age,main_language))
#     return name , age , main_language


# profile("유재석")
# profile("황광희")

#-----키워드
#순서가 바뀌어 있어도 무사히 호출이 가능

# def profile (name, age, height) :
#     print("이름{0},나이{1},키{2}cm".format(name,age,height))

# profile(age = 24, height=162, name="심훈용")


# -----가변인자

# def profile (name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {} \t 나이 : {} \t 언어 : {}".format(name,age), end="")   #end는 해당 명령어가 출력된 후 줄바꿈을 하지 않고 이어서 출력시켜줌.
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석",26,"C","C++","python")            #문제점 : 입력할 수 있는 언어 갯수는 5갠데 3개만 해놓으니 오류가 뜬다

# profile("유재석",26,"C","C++","python","","","")   # 꼭 이래야만 하는걸까? 혹은, 언어가 6개 이상이 되면? 이럴때 쓸 수 있는 것이 가변인자이다.


def profile (name, age, *language):             #*로 시작하는 변수를 도입함으로써 크기가 맘대로인 변수 생성 가능
    print("이름 : {0} \t 나이 : {1} \t 언어 : ".format(name,age), end="")  
    for i in language:
        print("{0}\t".format(i), end="")

profile("심훈용",24,"파이썬","자바","코틀린")