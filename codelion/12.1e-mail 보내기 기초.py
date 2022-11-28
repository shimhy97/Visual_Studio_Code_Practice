# SMTP = Simple Message Transfer Protocol

# 어떤식으로사용되는가?
# 클라이언트(우리) 서버A(내 메일 주소) 서버B(상대방 메일 주소)
# 클라이언트 -> 서버A <-> 서버 B <- 클라이언트 모두 SMTP 사용
# 다만, 외부에서 메일 받을때, 서버A -> 클라이언트로 가져와주는게 IMAP

# 평소 메일보낼때는 서버-서버 통신만 하므로 SMTP만 있으면 가능했음. 
# 하지만, 이번 경우는 다른게 파이썬 프로그램을
# 이용하여 메일을 보낼거기 때문에 수신받을때 IMAP이 필요함

# SMTP서버를이용해 우리가 원하는곳으로 메일을 보낼 수 있다.

# SMTP서버도 주소를 가지고 있다.!! Address와 Port로 구성됨.

# 학습목표: 1. SMTP 메일서버 연결
# 2. SMTP 메일 서버에 로그인
# 3. SMTP 메일 서버로 메일을 보낸다.


# SMTP 서버로 메일을 쉽게 보낼수 있게 해주는 라이브러리
import smtplib
import imghdr
# MIME이란? 메일을 보낼 때 이런 형태로 보낼꺼야!라고 SMTP에 전달해주는것.
# 이거 없으면 SMTP가 못알아들음. 즉 MIME형태로 메일을 변환시켜야함.
# 어떻게? email.message 모듈 사용. 그러기위해 import먼저해오자.
from email.message import EmailMessage

# SMTP함수는 서버와 연결을 해주는 함수. 서버를 찾아야함 . 
# 이러기 위해 주소와 포트번호 2가지 재료가 필요. 포트 번호는 문의 번호?  
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 #gmail에서 SMTP 쓰기 위해 지정한 문 번호.

# 그냥 출력하면 보안문제 때문에 오류 뜸. SSL이란것을 사용해야함.
# smtp = smtplib.SMTP(SMTP_SERVER,SMTP_PORT) <<<오류 발생

message = EmailMessage() #우리가 쓸 문자들을 MIME로 변환하여 저장하는 통

message.set_content("메일에뭐쓸지모르겠네.")#메일의 본문

# MIME엔 Header라는 것이 있다. 헤더엔 Subject From To 등이 있다
# 본문의 경우엔 헤더가 아니므로 set_content 쓴거임.
message["Subject"] = "이것은 제목입니다."
message["From"] = "shimhy1997@gmail.com"
message["To"] = "shimhy1997@gmail.com"

# ///이미지 첨부 하는 곳
with open("codelion.png","rb") as image: #with 사용하면 close 명령어 필요없음.
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)




smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) #SMTP_SSL 함수를 썼더니 이제 잘 출력됨.

smtp.login("shimhy1997@gmail.com","wkraud22!") #<<서버에 로그인 해주는 함수



smtp.send_message(message)
smtp.quit()


 
