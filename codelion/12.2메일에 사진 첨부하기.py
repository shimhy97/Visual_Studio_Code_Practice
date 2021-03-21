# 사진 자체를 파이썬 코드로 옮겨와야 함. 이럴때는 어떻게 하는가?

# 이미지를 컴퓨터가 읽을 수 있도록 표현해놓은것이 '바이너리'이다.

# r w a 대신 rb wb ab를 사용한 모드로 써야 한다.

# 메일에 이미지 첨부하려면
# add_attachment 함수를 사용해야함.
# mixed 타입은 이걸 무조건 쓴다.
# 텍스트가 아닌 다른 포맷의 파일이 같이 들어가면 mixed타입.
# 사진 첨부하면 mixed 타입이 되겠지?
# add_attachment() 사용하면 메일이 mixed가 됨

# add_attachment의 재료는 다음과 같이 3가지이다.
# 1.image
# 2.maintype = 첨부한 파일의 유형 ex. 이미지,비디오 등
# 3.subtype = 확장자 (codelion.png 의 경우 메인타입 = 이미지, 서브타입 = png)

# ex. 열려있는 파일 이름이 image_file인 경우,
# message.add_attachment(image_file,maintype='image',subtype='')

# 그런데 여기서 문제가 있다. subtype='png' 이래버리면 확장자 바뀔때마다 고생하자나?
# # 이미지 확장자가 변경되어도 알아서 넣는 작업을 해보자.
# >>import imghdr 모듈을 사용한다. 이는 이미지의 유형을 판단해주는 역할을 한다.
# 확장자가 변경되어도 동적으로 확장자를 가져오게 하려면 다음과 같이 한다.
# image_type = imghdr.what('파일명',image_file)