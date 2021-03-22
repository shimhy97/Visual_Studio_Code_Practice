딕셔너리는 키와 값을 가져오는 다양한 메서드를 제공합니다.

items: 키-값 쌍을 모두 가져옴
keys: 키를 모두 가져옴
values: 값을 모두 가져옴
다음과 같이 items()는 딕셔너리의 키-값 쌍을 모두 가져옵니다.

>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.items()
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
keys()는 키를 모두 가져옵니다.

>>> x.keys()
dict_keys(['a', 'b', 'c', 'd'])
values()는 값을 모두 가져옵니다.

>>> x.values()
dict_values([10, 20, 30, 40])
이 메서드들은 보통 for 반복문과 조합해서 사용하는데 자세한 내용은 뒤에서 설명하겠습니다.


///

리스트와 마찬가지로 딕셔너리도 할당과 복사는 큰 차이점이 있습니다. 먼저 딕셔너리를 만든 뒤 다른 변수에 할당합니다.

>>> x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> y = x
y = x와 같이 딕셔너리를 다른 변수에 할당하면 딕셔너리는 두 개가 될 것 같지만 실제로는 딕셔너리가 한 개입니다.

x와 y를 is 연산자로 비교해보면 True가 나옵니다. 즉, 변수 이름만 다를 뿐 딕셔너리 x와 y는 같은 객체입니다.

>>> x is y
True
x와 y는 같으므로 y['a'] = 99와 같이 키 'a'의 값을 변경하면 딕셔너리 x와 y에 모두 반영됩니다.

>>> y['a'] = 99
>>> x
{'a': 99, 'b': 0, 'c': 0, 'd': 0}
>>> y
{'a': 99, 'b': 0, 'c': 0, 'd': 0}
딕셔너리 x와 y를 완전히 두 개로 만들려면 copy 메서드로 모든 키-값 쌍을 복사해야 합니다.

>>> x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> y = x.copy()
이제 x와 y를 is 연산자로 비교해보면 False가 나옵니다. 즉, 두 딕셔너리는 다른 객체입니다. 그러나 복사한 키-값 쌍은 같으므로 ==로 비교하면 True가 나옵니다.

>>> x is y
False
>>> x == y
True