import random

x = int(input("로또를 몇 개 사나요? : "))

for i in range(x):
    num = random.sample(range(1, 46), 6)
    print(num)
