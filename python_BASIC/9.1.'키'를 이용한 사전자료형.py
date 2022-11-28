######################################################################################

#키와 열쇠 , 사전 자료형 {}

cabinet = { 1: "가렌", 2: "갈리오", 3:"갱플랭크"}

print( cabinet[1],cabinet.get(2))

#없는 키를 호출하면 오류가 뜨지만, .get 함수를 사용하면 None이 뜸
# print( cabinet[4])
print( cabinet.get(4))

#None 대신 다른 문자를 출력하고 싶다면?
print( cabinet.get(4,"4번키는없어용"))

#키가 있는 자료인지? 확인 가능한가?
print( 1 in cabinet)
print( 4 in cabinet)

#키는 문자 자료형도 가능하다.
Group = {"A": "나서스", "B": "가렌", "C": "유미"}
print(Group)
print(Group["A"],Group["B"])

#키에 저장된 자료의 변경
Group["A"] = "버프된 나서스"
Group["B"] = "버프된 가렌"
print(Group)

#키에 저장된 자료의 삭제

print(Group)

#Key들만 출력
print(Group.keys())

#Value들만 출력
print(Group.values())

#key와 value 모두를 출력
print(Group.items())

#다 지워!
print(Group.clear())