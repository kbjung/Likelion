#메뉴 리스트로 작성
#추가할 메뉴 입력 받기(q 입력하면 종료)
#제거할 메뉴 입력 받기(q 입력하면 종료)
#최종 리스트에서 랜덤으로 메뉴 고르기

import random
import time

menu = ["김치찌개","된장찌개","피자","짜장면"]

while True:
    print(menu)
    item = input("추가할 메뉴 입력하세요(종료는 'q'입력) : ")
    if item == "q":
        break
    else:
        menu.append(item)
print(menu)

set_menu = set(menu)

while True:
    print(set_menu)
    item = input("제거할 메뉴 입력하세요(종료는 'q'입력) : ")
    if item == "q":
        break
    else:
        set_menu = set_menu - set([item])
print(set_menu)

print(set_menu," 중 선택된 메뉴는")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_menu)))