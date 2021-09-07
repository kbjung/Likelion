import random
import time

lunch = ["짜장면","된장찌개","피자","호박죽"]

while True:
    print(lunch)
    item = input("추가할 메뉴를 메뉴를 입력하세요 : ")
    if item == "q":
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("제거할 메뉴를 입력하세요 : ")
    if item == "q":
        break
    else:
        set_lunch = set_lunch - set([item])
print(set_lunch)

item = random.choice(list(set_lunch))
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
print(item)