import random

def copmt_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)??").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f"The computer guessed our number, {guess}, correctly!")

copmt_guess(10)