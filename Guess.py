import random

_ = True
n = random.randint(1, 10)

while _:
    u = int(input("Guess an int number (1 to 10): "))
    if n != u:
        print("Wrong number! Try again.")
    else:
        print("Correct number! Congratulations!")
        _ = False