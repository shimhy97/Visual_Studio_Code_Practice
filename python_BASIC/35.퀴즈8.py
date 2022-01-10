#Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

#예제 
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년


class house :

    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.num = 0
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self): 
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type,self.deal_type, self.price, self.completion_year))


house_list = []         # 리스트 안에 클래스를 넣는 느낌으루다가 ㅎㅎ
num = 0 
list1 = house("강남","아파트","매매","10억","2010년")
list2 = house("마포", "오피스텔", "전세","5억","2007년")
list3 = house("송파", "빌라", "월세","500/50","2000년")

house_list.append(list1)
house_list.append(list2)
house_list.append(list3)

for i in house_list :
    num += 1
print("총 {0}대의 매물이 있습니다.".format(num))
for i in house_list : 
    i.show_detail()