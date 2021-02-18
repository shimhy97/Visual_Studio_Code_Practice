import re # 정규식 라이브러리 갖다 쓰자

#차가 사람을 치고 도망감. 뻉소니..?
#119에 신고, 차 뒤에 번호판. 네글자가 다 기억이 안남 ㅠㅠ 
#예를들어, ca?e 면 care cafe case cave 등을 경찰이 조사할것임.

#어떻게? caae, cabe, .....
p = re.compile("^ca") 

# . (ca.e): 하나의 문자를 의미함. ex: caae, case 등등  \ caffe 이런건 안됨
# ^ (^de): 문자열의 시작  ex: desk, destination 등등   \ fade 이런건 안됨
# $ (se$): 문자열의 끝 ex: case, base 등등 \ face 이런건 안됨
# 정규식은 엄청멏어첨 많은데, 이정도만 설명한다

# --------------------------------------------------------------------------------
def print_match(m) :     # m을 받는 함수인데, m에는 match, search, findall 등등 으로 받아온걸 저장
    if m:           # 매칭에 성공한 경우!!
        print("m.group():",m.group())
        print("m.string:", m.string)
        print("m.start():" ,m.start())
        print("m.end():" ,m.end())
        print("m.span():" ,m.span())
        
    else:           # 매칭이 안되는 경우, 즉 None!!!!
        print("매칭되지 않았습니다.")


# m = p.match("cafe") # match : 주어진 문자열의 처음부터 일치하는지 확인

m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인.

# m = p.findall("good carecaf") # findall : 일치하는 모든 것을 ★리스트★ 형태로 반환

print(m)
print(p)
print_match(m)


#총정리

# abcd = re.compile("원하는 형태")  ex. ca.e , ^de, se$ 등등

# abcd.match("비교할 문자열")   ex. case cafe caffe 등등
# abcd.search("비교할 문자열") 
# abcd_list("비교할 문자열") 등등



