#프로그램에서 사용하고 있는 데이터를 파일 형태로 저장함. 이를 가져와서 코드로 쓸 수 있음
# 즉, 피클 파일을 어떻게 생성하는 것이며, 어떻게 불러와서 출력할 수 있는지를 공부해보자.

# 쓰기
import pickle
profile_file = open ("profile.pickle", "wb")  # wb =  쓰기 목적의 w와 바이너리를 의미하는 b의 조합. 피클을 쓰기 위해선 항상 바이너리 타입이어야 한다.
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}  # 피클에 저장시킬 데이터
pickle.dump (profile,profile_file)   #★ pickle.dump(A,B)A의 정보를 B라는 피클 파일에 저장함!! 데이터의 정보를 지정한 피클 파일에 저장함.
profile_file.close()

# 읽기
profile_file = open ("profile.pickle", "rb")
profile = pickle.load(profile_file) # A = pickle.load(B)  ★ 피클 파일에 있는 정보를 profile에 불러오기
profile_file.close()
print(profile)

# ★----with---- close가 필요없다!
import pickle

with open("profile.pickle","rb") as profile_file :      # with open("A.pickle","rb") as B :데이터가 저장되어있는 피클 파일을 불러와서 변수에 저장하여 오픈함
    print(pickle.load(profile_file))                    # print( pickle.load(B)) 불러온 피클이 저장된 변수를 출력함. 이때 따로 close 불필요. 

with open("study.txt","w",encoding="utf8") as study_file:  #with open( "A.txt", "w", encoding="utf8") as B : 
    study_file.write("파이썬을 열심히 공부하고 있어요")     # B.write = "~~~"  /// B라는 변수를 만들어 그곳에 내용을 저장.

with open("study.txt","r",encoding="utf8") as study_file:  # with open( "A.txt","r",encoding="utf8") as B :
    print(study_file.read())                               # print(B.read())

