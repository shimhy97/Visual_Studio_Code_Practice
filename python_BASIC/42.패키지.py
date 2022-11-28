# 여러 모듈의 집합체 : 패키지

# 신규 여행사 프로젝트!

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


# from travel.thailand import ThailandPackage
from travel.thailand import *     ##주의!! 클래스나 함수는 바로 import를 할 수가 없다! travel.*** < 이부분엔 모듈이나 패키지만 가능.
                                    
trip_to = ThailandPackage()         
trip_to.detail()



from travel import vietnam 

trip_1 = vietnam.VietnamPackage()
trip_1.detail()


from travel import *  #이거 그냥 하면 왜 오류남? 폴더 내의 모듈파일을 불러올 시, 
                      # * 에 들어가는 모듈 항목들을 정의를 따로 해줘야 한다.. ㅠㅠ --> 폴더에 다른 파일을 생성해서 __all__ = []로 정의 해줘야 함.

trip_2 = thailand.ThailandPackage()
trip_2.detail()

import inspect
import random
print(inspect.getfile(random))              #경로 알려주는 함수
print(inspect.getfile(thailand))            #경로가 달라도 모듈 가져와서 쓸 수 있따 이말이야

# travel 폴더를 workspace가 아닌 다른 곳으로 옮겨도 동작할까? 응