
absent = [2,5]
nobook = [7]
for student in range (1,8) :
  if student in absent :              # list에 들어있다? in을 쓴다
    continue                          # continue는 그 아래 명령을 더이상 실행하지 않고 반복분의 처음으로 돌아가라는 의미인가봄.
  if student in nobook : 
    print("오늘 수업 여기서 끝, {0}, 너는 교무실로 따라와.".format(student))
    break                                                                      # break는 반복문을 그냥 탈출해버린다.
  print(f"{student}번, 나와서 읽어봐")
  
#한줄 FOR

student = [0,1,2,3,4,5]

student = [i+100 for i in student]

print(student)

list1 = ["aaa", "vvv", "ssssssss"]

list1 = [len(i) for i in list1]

print(list1)