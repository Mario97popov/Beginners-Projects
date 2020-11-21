import random

while True:
    base = True
    while base:
        num = input("Type a number: ")

        if num.isdigit():
            print("Let's play!")
            num = int(num)
            base = False
        else:
            print("Try Again!")

    number_to_be_guessed = random.randint(1, num)

    guess = None
    count = 1

    while guess != number_to_be_guessed:
        guess = input("Type number between 1 and " + str(num) + ": ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Type a number not a text!")
        if guess == number_to_be_guessed:
            print("You got it")
        else:
            print("Please try again!")
            count += 1
    print(f'It took you {count} guesses!')
