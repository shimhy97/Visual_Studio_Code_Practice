for waiting_no in [0,1,2,3,4] :  #반드시!!! :을 붙인다. 제발
    print( f"대기번호 : {waiting_no} ")

for waiting_no in range(1,6) :
    print( f"대기번호 : {waiting_no}")

#////

starbucks = ["아이언맨","토르","아이엠 그루트"]

for customer in starbucks :
    print(f"{customer}님, 커피가 준비되었습니다.")
    print("{0}님, 커피가 준비되었습니다.".format(customer))