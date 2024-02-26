import random

def guess(x):
    ran_num = random.randint(1, x)
    guess = 0
    while guess != ran_num:
        guess = int(input(f"Guess a numebr between 1 and {x}: "))
        if guess < ran_num:
            print("Guess again, Too Low.")
        elif guess > ran_num:
            print("Guess again, Too High.")
    print(f"Yay, you guessed it right: {ran_num}")
guess(10)