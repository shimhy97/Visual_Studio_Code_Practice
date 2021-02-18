#메딕은 공격유닛이 아님. 따라서 유닛 기본값에선 데미지 메서드를 빼고 공격유닛에만 데미지를 부여해보자.

class Unit:
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.armor = armor
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 방어력 {1}".format(self.hp,self.armor))

#공격 유닛
class AttackUnit(Unit):                         #상속받을 클래스를 괄호안에 적어준다.
    def __init__(self, name, hp, damage,armor):
        Unit.__init__(self, name, hp, armor)    #상속받는 부분!! Unit 클래스의 __init__ 메서드를 상속받아, 동일한 name, hp, armor 부분의 멤버 변수를 쓸 수 있다.
        self.damage = damage                    #추가로 공격력 부분을 정의할 수 있음        
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,6,0)


marine1 = marine()
marine2 = marine()

# medic1 = Unit("메딕",60,1)
# vulture = AttackUnit("벌쳐",80,20,0)
# vulture.damaged(5)
# vulture.damaged(5)
# vulture.damaged(5)
# vulture.damaged(5)


