# # input으로 입력 받은것은 무조건 str이다.

# # list 자료 추가하는법
# # append
# # insert = 원하는 곳에 추가

# list 자료 삭제하는 법

# del = index번호 입력받아 그 위치의 자료 삭제
# .remove = 자료 이릅 입력받아 해당 자료 삭제

# _list = "안녕하세요 심훈용입니다."

# for i in range(len(_list)):
#     try:
#         if _list[i] == "":
#             print("",end="")
#         else:
#             print(_list[2*i+1])
#     except IndexError:
#         break

orders = ["짜장", "짬뽕", "탕수육"]

food = input("먹고싶은 메뉴를 입력해주세요 : ")

if food in orders : # 리스트에 변수가 있느냐
    print("주문할 수 있습니다.")
else :
    print("주문할 수 없습니다.")

# while + continue 조합으로 흐름 제어 하는법!!

# range 함수의 스텝(시작숫자, 종료숫자, 스텝)