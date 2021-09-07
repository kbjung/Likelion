import random

count = int(input("로또를 몇개 구매하시겠습니까? "))

for i in range(count) :
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)

print("로또 종료")