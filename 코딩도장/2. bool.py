이번에는 is와 is not입니다. 같다는 ==, 다르다는 !=이 이미 있는데 왜 is, is not을 만들었을까요? is, is not도 같다, 다르다지만 ==, !=는 값 자체를 비교하고, is, is not은 객체(object)를 비교합니다(객체에 대해서는 'Unit 34 클래스 사용하기'에서 자세히 설명하겠습니다).

>>> 1 == 1.0
True
>>> 1 is 1.0
False
>>> 1 is not 1.0
True
1과 1.0은 정수와 실수라는 차이점이 있지만 값은 같습니다. 따라서 ==로 비교해보면 True가 나옵니다. 하지만 1과 1.0을 is로 비교해보면 False가 나옵니다. 왜냐하면 1은 정수 객체, 1.0은 실수 객체이므로 두 객체는 서로 다르기 때문입니다. 물론 1과 1.0을 is not으로 비교하면 True가 나오겠죠?

참고 | 정수 객체와 실수 객체가 서로 다른 것은 어떻게 확인하나요?
정수 객체와 실수 객체가 서로 다른지 확인하려면 id 함수를 사용하면 됩니다. id는 객체의 고유한 값(메모리 주소)을 구합니다(이 값은 파이썬을 실행하는 동안에는 계속 유지되며 다시 실행하면 달라집니다).

>>> id(1)
1714767504
>>> id(1.0)
55320032
두 객체의 고유한 값이 다르므로 서로 다른 객체입니다. 그래서 1과 1.0을 is로 비교하면 False가 나옵니다. is, is not은 클래스로 객체를 만든 뒤에 객체가 서로 같은지 비교할 때 주로 사용합니다.

여기에 나오는 객체의 고유한 값(메모리 주소)에 대해서는 신경 쓸 필요 없습니다. ==, !=와 is, is not의 동작 방식이 다르다는 정도만 알아 두면 됩니다.

참고 | 값 비교에 is를 쓰지 않기
값을 비교할 때는 is를 사용하면 안 됩니다. 다음과 같이 변수 a에 -5를 할당한 뒤 a is -5를 실행하면 True가 나오지만 다시 -6을 할당한 뒤 a is -6을 실행하면 False가 나옵니다.

>>> a = -5
>>> a is -5
True
>>> a = -6
>>> a is -6
False
왜냐하면 변수 a가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라질 수 있기 때문입니다. 따라서 다른 객체가 되므로 값이 같더라도 is로 비교하면 False가 나옵니다. 값(숫자)를 비교할 때는 is가 아닌 비교 연산자를 사용해야 합니다.



참고 | 정수, 실수, 문자열을 불로 만들기
정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 됩니다. 이때 정수 1은 True, 0은 False입니다. 만약 문자열의 내용이 'False'라도 불로 만들면 True입니다. 문자열의 내용 자체는 판단하지 않으며 값이 있으면 True입니다.

bool(값)

>>> bool(1)
True
>>> bool(0)
False
>>> bool(1.5)
True
>>> bool('False')
True
즉, 정수 0, 실수 0.0이외의 모든 숫자는 True입니다. 그리고 빈 문자열 '', ""를 제외한 모든 문자열은 True입니다.