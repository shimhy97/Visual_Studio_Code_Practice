
class Unit:
    def __init__(self, name, hp, armor, speed):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))    
    
    def move(self, location):
        print("지상 유닛을 이동하겠습니다. ")
        print("{0} : {1} 방향으로 이동합니다. 이동속도 :{2}".format(self.name,location,self.speed))   
      
#공격 유닛
class AttackUnit(Unit):                        
    def __init__(self, name, hp, damage, armor, speed):
        Unit.__init__(self, name, hp, armor,speed)    
        self.damage = damage                         

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flyingspeed) :
        self.flyingspeed = flyingspeed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flyingspeed))


class FlyableAttackUnit(AttackUnit,Flyable):            
    def __init__(self, name, hp, damage, armor, flyingspeed) :   
        AttackUnit.__init__(self, name, hp, damage, armor,0)      
        Flyable.__init__(self, flyingspeed)                      
        print("체력 {0}, 방어력 {1}, 공격력 {2}, 비행 속도 : {3}".format(self.hp,self.armor,self.damage,self.flyingspeed))

    def move(self, location):
        print("공중 유닛을 이동하겠습니다.")
        self.fly(self.name, location)


#건물

class BuildingUnit(Unit):
    def __init__(self, name, hp, armor, location):
        # Unit.__init(self, name, hp, armor, 0 )      #클래스를 상속받아 초기화를 할때는 값을 넣어줌으로써 초기화를 해줬었지.
        super().__init__(name, hp, armor, 0)          #super를 통해 초기화 하는 부분이다. ()를 쓰고 self를 넘기지 않는다는 것이 다르다.
                                                  # 근데 다중상속 할때 문제점이 생긴다. 다음 파일에서 살펴보자.
        self.location = location
        print("{0} : 체력 = {1}, 방어력 = {2}, 건설 위치 = {3}".format(self.name,self.hp, self.armor, location))

#서플라이 디팟

supplydepot = BuildingUnit("서플라이 디팟", 500, 1, "7시")

