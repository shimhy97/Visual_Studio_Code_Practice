class Unit:
    def __init__(self, a, b, c): #
        self.name = a
        self.hp = b
        self.damage = c
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#멤버 변수는 클래스 내에서 self.변수 형식으로 표현된 것들을 의미함.

wraith1 = Unit("레이스",120,8)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

#마컨
#파이썬에서는 클래스 외부에서 추가로 뭘 더 만들어서 확장하여 쓸 수 있다.
#다만 확장된 변수는 내가 확장한 변수에만 적용이 되고 다른 객체에는 적용이 안됨.

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")
    print(f"{wraith2.hp}는 120이며 데미지는 {wraith2.damage}입니다.")