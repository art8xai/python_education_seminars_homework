# Program for playing candy. Player vs bot.
#
# Conditions:
# The game starts with 120 candies. Players make moves one after the other. The person takes the first step. In one
# move, you can take no more than 28 candies. The one who left 0 candies on the table wins.

import random


def get_checked_move(candies: int) -> int:
    """Return the move if the conditions are met."""
    while True:
        try:
            number_player = int(input('Player move: '))
        except ValueError:
            print('Sorry, you entered an invalid value, please try again...')
        else:
            if number_player > candies:
                print('Sorry, you entered a value greater than the number of available candies, please try again...')
                continue
            if number_player in range(1, 29):
                return number_player
            else:
                print('Sorry, you entered a value out of the available range, please try again...')


def play_game(candies: int, move: bool, bot_difficulty: bool):
    """Play the game."""
    print()
    while candies > 0:
        print(f'Candy left: {candies}\n')
        if move:
            candies = candies - get_checked_move(candies)
            if candies == 0:
                print('Player wins! Congratulations!')
            move = False
        else:
            if candies <= 28:
                number_bot = candies
                candies -= number_bot
                print(f'Bot move: {number_bot}')
                print('Bot won!')
                break
            else:
                if not bot_difficulty:
                    number_bot = random.randint(1, 28)
                    candies -= number_bot
                    move = True
                else:
                    i = 57
                    while True:
                        if candies <= i:
                            number_bot = candies - i + 28
                            if number_bot == 0:
                                number_bot = random.randint(1, 28)
                            candies -= number_bot
                            move = True
                            break
                        i += 29
            print(f'Bot move: {number_bot}')


while True:
    print()
    print('WELCOME TO THE CANDY GAME!')
    print('In one move, you can take no more than 28 candies. The one who left 0 candies on the table wins.')
    candies_source = 120
    move_source = True
    # If you need to determine who will be the first to move randomly, uncomment this comment (two options are given):
    # move_source = True if random.random() > 0.5 else False
    # move_source = random.choice([True, False])
    while True:
        try:
            difficulty_input = int(input(
                'Select the difficulty of the game by entering a number (0 - easy, 1 - hard): '))
        except ValueError:
            print('Sorry, you entered an invalid value, please try again...')
        else:
            if difficulty_input in range(0, 2):
                break
            else:
                print('Sorry, you entered a value out of the available range, please try again...')
    if difficulty_input == 0:
        bot_difficulty_source = False
    else:
        bot_difficulty_source = True
    play_game(candies_source, move_source, bot_difficulty_source)
    print()
    answer = input('Do you want to play again? (Y/N) ')
    if answer.lower() == 'y':
        continue
    else:
        break
