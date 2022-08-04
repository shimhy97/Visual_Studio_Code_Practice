from hashlib import new
import re

def solution(new_id):
    
    #1단계 : 대문자 > 소문자
    new_id = new_id.lower()

    #2단계 : 소문자 숫자 빼기 밑줄 마침표 제외 모두 제거
    con2 = '[^a-z0-9-_.]'
    new_id = re.sub(con2,"",new_id)
    
    #3단계 : .. 처럼 . 2개 이상 => 하나의 .
    while new_id.count("..") != 0:
        new_id = new_id.replace("..",".")

    #4단계 : 처음이나 끝에 있는 마침표 제거
    con4 = '^[.]+|[.]+$'
    new_id = re.sub(con4,"",new_id)
    
    #5단계 : 빈 문자열이라면 "a"
    if new_id == '' : new_id = "a" 
    
    #6단계 : 16자 이상이라면 초과 문자 뒤에꺼 제거, 이후 4단계 실행
    con6 = '[.]+$'
    max_len = 15
    new_id = re.sub(con6,"",new_id[:max_len]) if len(new_id)>=max_len else new_id

    #7단계 : 2자 이하라면 3자가 될때까지 마지막문자를 추가
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]

    answer = new_id
    
    return answer


ans_list = ["...!@BaT#*..y.abcdefghijklm","z-+.^.","=.=","123_.def","abcdefghijklmn.p"]

for x in ans_list:
    print(solution(x))