# super(). 를 이용한 초기화 방식의 문제점
# 다중 상속의 경우, 초기화가 앞에 써진 하나만 된다.
# 예를 들어..

class unit:
    def __init__(self):
        print("유닛 생성자")

class flyable:
    def __init__(self):
        print("공중유닛 생성자")

class flyableUnit(flyable, unit):   # 이 부분에서 상속 순서에 따라 super가 무엇을 상속할지 딱 하나만 결정되게 된다. 두개 다 상속하려면 어떻게 해?
    def __init__(self):             # ->그냥 super 안쓰는 방식으로 하면 됨..
        # super().__init__()
        unit.__init__(self)
        flyable.__init__(self)

        
dropship = flyableUnit()   


