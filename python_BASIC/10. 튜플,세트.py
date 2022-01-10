# 튜플 (A,B,C)
# 튜플은 리스트와 다르게 삭제 추가가 안됨
# 그럼 왜쓰냐? 속도가 리스트보다 빠름.
menu = ("돈까스","치즈까스")

print(menu[0])
print(menu[1])

#menu.add("생선까스")    오류 뜸

#장점?

# name = "김종국"
# age = 20
# hobby = "코딩"

(name, age, hobby )= ("김종국",20,"코딩")
print(name, age, hobby)


#------------------------
#집합 {A,B,C} 혹은 set([A,B,C]) 즉 set[리스트]
#순서 상관 X
#중복 자료 무시

java = {"유재석","양세형","아이린"}

python = set(["유재석", "박명수", "예지"])          # 집합 정의 방식 두가지

print(java & python)
print(java.intersection(python))
print(java | python)
print(java.union(python))
print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

python.remove("김태호")
print(python)