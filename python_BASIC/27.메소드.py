#클래스 내부에 정의된 함수를 메서드 라고 부른대

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage): #셀프는 자기 자신을 의미한다. 클래스 내에서 메서드 앞에선 무적권 self를 적음
        self.name = name
        self.hp = hp
        self.damage = damage               
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))  #self를 붙이면 클래스 자기 자신에 있는 멤버 변수 값을 출력함.

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)