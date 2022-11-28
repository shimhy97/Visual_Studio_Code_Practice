def solution(s):
    
    dct = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    dct = {v: k for k, v in dct.items()}
    change_int_to_num = list(map(str,dct.values()))
    bin = ""
    # 문자열 돌면서 영단어 추가
    for n, i in enumerate(s):
        if i in change_int_to_num:
            continue

        bin+=i

        # dct에 있는지 체크
        # 있으면 숫자로 변경
        if bin in list(dct.keys()):
            s = s.replace(bin,str(dct[bin])) 
            bin = ""
        
    answer = int(s)
    return answer



solution("one4seven")