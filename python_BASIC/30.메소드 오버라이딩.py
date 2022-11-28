#부모 클래스에서 정의한 변수 말고 자식 클래스에서 정의한 변수를 쓰고 싶을 때, 메소드를 새롭게 정의해서 사용할 수 있는데! 이를 오버로딩이라 한다.

class Unit:
    def __init__(self, name, hp, armor, speed):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))    
    
    def move(self, location):       #추가된 부분
        print("지상 유닛을 이동하겠습니다. ")
        print("{0} : {1} 방향으로 이동합니다. 이동속도 :{2}".format(self.name,location,self.speed))   
        #주의!! 지상유닛에 속도 정보가 없어서, speed 멤버를 새로 추가했는데, 이러면 상속받는 곳에서도 전부 수정해줘야 한다.

#공격 유닛
class AttackUnit(Unit):                        
    def __init__(self, name, hp, damage, armor, speed):
        Unit.__init__(self, name, hp, armor,speed)    
        self.damage = damage                         

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))

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
        AttackUnit.__init__(self, name, hp, damage, armor, 0)      #지상 스피드의 경우 이미 있으니까, 멤버 초기화 자리에 0을 써준다
        Flyable.__init__(self, flyingspeed)                      
        print("체력 {0}, 방어력 {1}, 공격력 {2}, 비행 속도 : {3}".format(self.hp,self.armor,self.damage,self.flyingspeed))

    def move(self, location):               # 여기부터 다른 점! 유닛에 있는 메서드인 move를 재정의 하겠다..! 이러면 이제 앞으로 Unit의 move가 아닌 FlyableAttackUnit의 move가 호출됨.
        print("공중 유닛을 이동하겠습니다.")
        self.fly(self.name, location)       # 이 부분이 다른 점





#벌쳐 : 지상 유닛, 기동성이 좋음

vulture1 = AttackUnit("벌쳐",80,20,0,10)
vulture1.move("1시")

Goliath1 = AttackUnit("골리앗",125,12,1,4)
Goliath1.attack("2시")
Goliath1.move("2시")
Goliath1.damaged(10)

#배틀크루저 : 

battlecruiser1 = FlyableAttackUnit("배틀크루저",500,25,3,3)
battlecruiser1.fly(battlecruiser1.name,"9시")  # 형식 주의깊게 살펴볼것.

#여기서 불편한 점!!! 매번 공중유닛과 지상유닛을 구별(move,fly)해줘야 하는 불편함이 있다!!
#메소드 오버라이딩을 통해 똑같이 move 메소드만 쓰면 지상의 경우 이동, 공중의 경우 날아가는 처리를 해보자.

battlecruiser1.move("9시")
