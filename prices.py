import random

price = 100
for x in range(0, 3):
    r = random.random()
    print("my random number is:", r)
    price = price + r
    print("my new price is:", price)