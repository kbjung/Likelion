menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

food = input("먹고싶은 메뉴를 입력해주세요 : ")

if food in menu :
    print(menu[food], "원 입니다.")
else :
    print("주문 불가")