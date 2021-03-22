# 원하는 키나 밸류값 삭제하기


keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))
 
x = { key:value for key,value in x.items() if key!='delta' and value != 30 } 

print(x)


# 참고 ! key를 기준으로 삭제할 때는 x.pop('키 이름') 혹은 del x['키 이름'] 을 사용하는 것이 좋다.