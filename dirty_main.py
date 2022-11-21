from random import randint


def get_money():
    print("Бюджет равен ", end="")
    print(randint(10_000, 1_000_000))
