# guess the number which the computer chooses
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number b/w 1 and {x}: "))
        if guess < random_number:
            print("sorry, guess again. too low")
        elif guess > random_number:
            print("sorry, guess again, too high")
    print(f"you guessed the number {random_number} correctly")


guess(10)
