#질문 입력
#답변 입력
#딕셔너리 출력

total_dictionary = {}

while True:
    question = input("질문을 입력해주세요('q'를 입력하면 종료) : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력하세요('q'를 입력하면 종료) : ")
    total_dictionary[i] = answer

print(total_dictionary)