
import time
import random

menu_list = ["된장찌개","피자","제육볶음","짜장면"]

menu_set = set(menu_list)
# print(f"점심 메뉴 후보 : {menu_set}")

def add_food(menu_set):
    while True:
        a = input("음식을 추가 해주세요(끝내기 : q) : ")
        if a =="q":
            return menu_set
        else :
            menu_set = menu_set.union(set([a]))
            print(f"현재 메뉴는 {menu_set}입니다. ")
    return menu_set

def delete_food(menu_set):
    while True:
        a = input("음식을 삭제 해주세요(끝내기 : q) : ")
        if a =="q":
            break
        elif a not in menu_set:
            print("메뉴에 없는 목록입니다.")
        else :
            menu_set = menu_set.difference(set[a])
            print(f"현재 메뉴는 {menu_set}입니다. ")
    print(f"최종 메뉴 후보군은 {menu_set}입니다.")
    return menu_set

def choice_food(menu_set):
    for i in range(6):
        print(f"{5-i}초후에 공개됩니다.")
        time.sleep(1)
    menu_list = list(menu_set)
    print("오늘의 점심 메뉴는~~ {0}입니다".format(random.choice(menu_list)))

menu_set = add_food(menu_set)
menu_set = delete_food(menu_set)
choice_food(menu_set)

#  중요하게 배운 것 : 변수 연산을 하고, 저장을 빼먹지 말것.