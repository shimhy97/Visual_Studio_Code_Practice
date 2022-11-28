#외장함수 : import를 해와야만 사용이 가능한 함수

#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir 명령어와 똑같음.)
import glob
print(glob.glob("*.txt")) # 확장자가 py인 모든 파일

#os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dirrrr"

if os.path.exists(folder):                  # path.exists : 존재하는지?
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)                        # rmdir :  폴더 삭제
    print(folder,"폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)                     # makedirs : 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())     #listdir() : 디렉토리 파일 명들을 출력해줌

import time         # 시간 관련 함수 제공
print(time.localtime())
print(time.strftime("%y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today()) #오늘 날짜 출력

today = datetime.date.today()       #오늘 날짜 저장
td = datetime.timedelta(days=30000)       # 100일 저장. 날짜의 덧셈뺄셈을 하고싶을때 이 함수 쓰는듯.
print( today + td )
