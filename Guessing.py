import random

def guess_the_number():

    number = random.randint(1, 20)

    guesses = 5

    while guesses > 0:

        guess = int(input("Guess a number between 1 and 20: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:

            print("Yeah!", number)
            break

        guesses -= 1

        if guesses == 0:
            print("Sorry, The number was", number)

guess_the_number()