lunch = ["된장찌개","피자","짜장면","치킨"]

while True:
    print(lunch)
    item = input("추가할 메뉴를 입력하세요 : ")
    if item == "q":
        break
    else:
        lunch.append(item)

print(lunch)