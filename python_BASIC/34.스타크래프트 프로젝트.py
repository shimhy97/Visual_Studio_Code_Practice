
class Unit:
    def __init__(self, name, hp, armor, speed):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))    # self.name을 쓰던 name을 쓰던 상관은 없다. (매개변수, paramater(self))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. 이동속도 :{2}".format(self.name,location,self.speed))   

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


#공격 유닛
class AttackUnit(Unit):                        
    def __init__(self, name, hp,  damage, armor, speed ):
        Unit.__init__(self, name, hp, armor,speed)
        self.damage = damage                         
        print("HP = {0}, 공격력 = {1}, 방어력 = {2}, 지상 이동속도 = {3}".format(self.hp,self.damage,self.armor,self.speed))
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(self.name, location, self.damage))


class Flyable:
    def __init__(self, flyingspeed) :
        self.flyingspeed = flyingspeed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flyingspeed))


class FlyableAttackUnit(AttackUnit,Flyable):            
    def __init__(self, name, hp, damage, armor, flyingspeed) :   
        AttackUnit.__init__(self, name, hp, damage, armor,0)      
        Flyable.__init__(self, flyingspeed)                      

    def move(self, location):
        self.fly(self.name, location)

    def init(self) :
        self.__init__
        print("HP = {0}, 공격력 = {1}, 방어력 = {2}, 비행속도 = {3}".format(self.hp,self.damage,self.armor,self.flyingspeed))
        

#////////////유닛 클래스

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40, 6 ,0 ,3)  # self 빼먹지마라 제발 ㅋㅋ

    def stimpack(self):   # 편의상 공격력 증가로 바꾸자
        if self.hp > 10:
            self.hp -=10
            self.damage +=1
            print("스팀팩을 사용합니다. 현재 체력은 {0}입니다.".format(self.hp))
        elif self.hp <= 10:
            print("현재 HP가 너무 낮아 스팀팩을 사용할 수 없습니다.")



class Tank(AttackUnit):
    seize_developed = True
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,30,1,3)
        self.seize_mode = False
     
    def set_seize_mode(self):
        if self.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("시즈모드로 전환합니다.")
            self.damage *= 2
            self.speed = 0
            self.seize_mode = True
        else :
            print("시즈모드를 해제합니다.")
            self.damage /= 2
            self.speed = 3
            self.seize_mode = False
        

class Wraith(FlyableAttackUnit):
    
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",120,8,0,8)
        print("비행속도 = {0}".format(self.flyingspeed))
        self.clocked = False
    
    def clocking(self):
        if self.clocked == False :
            self.clocked = True
            print("클로킹 상태에 진입합니다. 은신 효과가 추가됩니다.")
        else :
            self.clocked = False
            print("클로킹 상태가 해제됩니다.")



def game_start():
    print("[알림] : 새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#실제 게임 진행

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

attack_units = [m1,m2,m3,t1,t2,w1]

for i in attack_units :
    i.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("시즈모드 개발 완료")

#공격 모드 준비
for i in attack_units : 
    if isinstance(i, Marine) :            # 어떤 클래스의 인스턴스인가? 해당 클래스에 따른 분기점 생성
        i.stimpack()
    elif isinstance(i,Tank):
        i.set_seize_mode()
    elif isinstance(i,Wraith) : 
        i.clocking()

for i in attack_units :
    i.attack("1시")

from random import *

for i in attack_units:
    i.damaged(randint(5,21))

#게임 종료

game_over()