요소가 한 개인 튜플을 만들 때는 ( )(괄호) 안에 값 한 개를 넣고 ,(콤마)를 붙입니다. 
또는, 괄호로 묶지 않고 값 한 개에 ,를 붙여도 됩니다.

튜플 = (값, )
튜플 = 값,
>>> (38, )
(38,)
>>> 38,
(38,)
튜플은 요소를 변경, 추가, 삭제할 수도 없는데 값 한 개짜리 튜플은 왜 필요할까요? 
함수(클래스)를 사용하다 보면 값이 아닌 튜플을 넣어야 할 경우가 생깁니다. 
이때 값은 한 개지만 튜플을 넣어야 할 때 (값, )과 같은 형식을 사용해야 합니다. 
실무에서는 가끔 이 문법을 사용하게 되는데, 그냥 튜플 형태를 유지하기 위한 문법이라고 생각하면 됩니다.


//////
사실 '6.4 입력 값을 변수 두 개에 저장하기'에서 사용한 input().split()은 리스트를 반환합니다. 
그래서 리스트 언패킹 형식으로 입력 값을 변수 여러 개에 저장할 수 있었습니다.