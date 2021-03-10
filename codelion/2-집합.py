집합은 리스트와 다르게, 중복 X 그리고 순차적요소로 접근 못함.

https://python-reference.readthedocs.io/en/latest/docs/sets/

집합의 큰 기능? 집합의 연산이 가능함.

출력할때마다 출력순서는 바뀜, 하지만 지장은 없음/

포함관계에 대한 Boolean 연산자 
<= >= = 등등 사용 가능. (집합의 포함 관계 의미함)

| -  &(교집합)  ^(여집합) 등으로 집합의 연산 가능 

ex.
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 & menu2
print(menu3)