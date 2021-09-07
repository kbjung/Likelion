#질문을 입력
#해당 질문에 대한 답변 입력

total_list = []

while True:
    question = input("무엇이 궁금한가요?('q'입력하면 종료) : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question,"답변" : ""})

for i in total_list:
    answer = input(i["질문"])
    i["답변"] = answer

print(total_list)