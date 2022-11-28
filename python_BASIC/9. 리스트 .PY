# 리스트 [] : 순서를 가지는 변수

SU1=10
SU2=20
SU3=30

subway = [10,20,30]
print( subway )

subway = ["유재석","조세호","박명수"]

# 조세호는 몇번째 칸에 타고 있지?
print("조세호씨는 "+ str(subway.index("조세호")+1)+"번째 칸에 타고 있습니다.")

#끝부분에 자료 추가하고 싶을때 -> append
subway.append ("하하")
print (subway)

#중간에 자료 추가하고 싶을때 -> insert(넣을 위치, 추가할 자료 이름)
subway.insert(1, "정형돈")
print(subway)            #//두번째 칸에 정형돈이 추가됨

#자료를 꺼내고 싶을 때 -> pop (뒤에서부터 자료 하나씩 꺼냄, append의 반대)
print(subway.pop())
print(subway.pop())
print(subway.pop())     #꺼내지는 자료 출력, 여기서는 하하,박명수,조세호
print(subway)        #꺼내진 후 남은 자료 출력.

# #숫자도 셀 수 있음.
subway.append("유재석")
print( subway )
#리스트 내에 "유재석"은 몇 번 들어가있는가?
print( "리스트 내부에 유재석은 " + str(subway.count("유재석")) + "번 들어가 있습니다.")


#정렬 하는 방법 -> .sort
nulist = [5,2,3,4,1]
nulist.sort()          # nulist의 변수들을 크기순서대로 정렬
print(nulist)          # 주의!!! print( nulist.sort()) 하면 안됨

#순서 뒤집기 기능 -> .reverse
nulist.reverse()
print(nulist)          # 주의!!! print( nulist.reverse() 하면 안됨)

#리스트 내부 싹 다 지우기 -> .clear
# nulist.clear()
# print(nulist)

#리스트는 다양한 자료 유형에 대해 사용 가능하다.
nulist2 = [True,1,"유재석",6>3]
print (nulist2)

# #서로 다른 두 리스트 합치기  -> .extend
nulist.extend(nulist2)
print(nulist)

