lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
set_lunch = set(lunch)

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    lunch.append(item)
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)
