name = "마린"
hp = 40
damage = 5

print(f"{name}이 생성되었습니다.")
print(f"체력은 {hp}, 공격력은 {damage} 입니다.")


name_2 = "탱크"
hp_2 = 150
damage_2 = 30

print(f"{name_2}이 생성되었습니다.")
print(f"체력은 {hp_2}, 공격력은 {damage_2} 입니다.")

def attack (name, location, damage):
    print(f"{name}유닛이 {location} 방향으로 {damage}의 데미지를 줍니다.")
    
attack(name,"1시",damage)
attack(name_2,"1시",damage_2)

#그런데 유닛이 생성될 때 마다 이 짓을 반복하냐? 어렵다.. 여기서 클래스 개념이 나온다.
#붕어빵 틀이라고 생각하자.