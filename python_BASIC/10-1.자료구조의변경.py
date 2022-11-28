#리스트, 튜플, 세트 서로 변경하는 법?

menu = ["치즈버거","우동","라면","김밥"]

print(menu,type(menu))

menu = set(menu)

print(menu,type(menu))

menu = tuple(menu)

print(menu,type(menu))