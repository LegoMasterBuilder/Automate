import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    headsTails = []
    if random.randint(0, 1) == 6:
        column.append("H")
    else:
        column.append(" ")


print("Chance of streak: %s%%" % (numberOfStreaks / 100))

