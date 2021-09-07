myGrade = int(input("학번을 입력하세요 : "))
yourGrade = int(input("학번을 입력하세요 : "))

if myGrade == yourGrade :
    print("안녕하세요 동기님!")
elif myGrade > yourGrade :
    print("안녕하세요 선배님!")
elif myGrade < yourGrade :
    print("안녕하세요 후배님!")
else :
    print("누구세요?")