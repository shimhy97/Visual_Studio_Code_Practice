#메딕은 공격유닛이 아님. 따라서 유닛 기본값에선 데미지 메서드를 빼고 공격유닛에만 데미지를 부여해보자.

class Unit:
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.armor = armor
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        

#공격 유닛
class AttackUnit(Unit):                         #상속받을 클래스를 괄호안에 적어준다.
    def __init__(self, name, hp, damage,armor): #AttackUnit의 __init__메서드는 이렇게 !변수! 받아서 정의할거얌~~ 
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


#부모가 둘 이상이면 다중상속이라고 한다.!!!!!!
#공중유닛은 일반적인 유닛의 특성 + 날수 있는 특성
#또한 공격 공중유닛 + 비공격 공중유닛 등등

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flyingspeed) :
        self.flyingspeed = flyingspeed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flyingspeed))

#날 수 있는 공격 유닛
class FlyableAttackUnit(AttackUnit,Flyable):            # 다중상속 받음. 제공받은 각 클래스의 메서드를 다 쓸 수 있음.
    def __init__(self, name, hp, damage, armor, flyingspeed) :   #초기화!!
        AttackUnit.__init__(self, name, hp, damage, armor)       #또 초기화!!
        Flyable.__init__(self, flyingspeed)                      #또또 초기화!!!
        print("체력 {0}, 방어력 {1}, 공격력 {2}, 비행 속도 : {3}".format(self.hp,self.armor,self.damage,self.flyingspeed))


#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.

valkyrie = FlyableAttackUnit("발키리", 200, 6, 2, 5) # 변수에 클래스 호출함
valkyrie.fly(valkyrie.name, "3시")                   # 변수이름.메서드이름(성분1,성분2,...)
