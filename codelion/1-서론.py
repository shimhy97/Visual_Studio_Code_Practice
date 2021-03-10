import time
import random

information =  {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}

print(random.choice(information))

print(information.get("고향"))


information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"]
print(information.get("취미"))
information["특기"] = "피아노"
information["사는곳"] = "서울"     #와 이렇게 추가하는구나. 정의만 해주면 알아서 딕셔너리에 반영되네.
del information["좋아하는 음식"]   # 키 삭제
print(information)
print(len(information))
information.clear()
print(information)
print(foods[-2])
foods.append("김밥")
del foods[1]
print(foods)

empty=[]
for i in information:
    empty[i] = information[i]


information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x, y in information.items():
    print(x)
    print(y)
