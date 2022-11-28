#score.txt 라는 파일을 쓰기 목적(w)으로 열어서 쓰고 창을 닫는거까지

score_file = open("score.txt", "w", encoding="utf8")             # 열었으면 닫아야지! 습관
print("수학:0점", file = score_file)
score_file.close()


score_file = open("score.txt", "w", encoding = "utf8")        # "w"는 처음부터, "a"는 이어서 작성한다는 뜻임 
score_file.write("수학 = 0점\n경제 = 100점\n수학 = 0점\n과학 = 100점\n 도덕 = 0점\n사회 = 100점\n") 
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print( score_file.read(),end="")    # 한번에 모든 줄 다 읽기.
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(),end="") # ★줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동, 커서 이동을 원하지 않는가면 ,end="" 추가
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()


# # --몇줄인지 모를때?

score_file = open("score.txt","r", encoding="utf8")
lines = score_file.readlines()   # list 형태로 일단 내용을 저장함!
for i in lines :                 # 한줄 씩 읽어
    print(i, end="")
score_file.close()