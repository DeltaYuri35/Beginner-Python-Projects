import random


def play():
    user = input("What's your choice? \n'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return "You Won!"

    return "You lost"


def is_win(player, opp):
    if (player == 'r' and opp == 's') or (player == 's' and opp == 'p') \
            or (player == 'p' and opp == 'r'):
        return True


print(play())
