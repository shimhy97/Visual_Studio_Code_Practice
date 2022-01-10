class Unit:
    def __init__(self, name, hp, damage): #메서드를 정의할 땐 항상 self 인자를 써 준다.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 클래스 사용법

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank1 = Unit("탱크",150,30)
tank2 = Unit("탱크",150,30)

#이때 정보를 적게 넘기면 오류 남
