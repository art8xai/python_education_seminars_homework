# Program for playing tic-tac-toe. Player vs player.

from colorama import init, Fore

init(autoreset=True)


def get_fields() -> list:
    """Return empty fields."""
    return list(range(1, 10))


def print_board(lst: list):
    """Print the state of the fields to the console in the form of a playing field."""
    # For ease of dialing, the arrangement of numbers corresponds to the numbering on the calculator.
    print()
    for i in range(2, -1, -1):
        for j in range(0, 3):
            if lst[j + i * 3] == 'X':
                print(Fore.RED + chr(88), end='')
            elif lst[j + i * 3] == 'O':
                print(Fore.GREEN + chr(79), end='')
            else:
                print(lst[j + i * 3], end='')
            if j != 2:
                print(end=' | ')
        print()
        if i != 0:
            print('--+---+--')
    print()


def make_move(value: str, lst: list):
    """Make a move."""
    while True:
        user_request = input(f'Please select a field to put a "{value}" (enter a number): ')
        try:
            user_request = int(user_request)
        except ValueError:
            print('Sorry, you entered an invalid value, please try again...')
            continue
        if 1 <= user_request <= 9:
            if str(lst[user_request - 1]) not in 'XO':
                lst[user_request - 1] = value
                break
            else:
                print('Sorry, this field is busy, please try again...')
        else:
            print('Sorry, you entered a value out of range, please try again...')


def get_check_winner(lst: list) -> str or bool:
    """Return a winning value or return false."""
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for t in win_comb:
        if lst[t[0]] == lst[t[1]] == lst[t[2]]:
            return lst[t[0]]
    return False


def play_game(lst: list):
    """Play the game."""
    count = 0
    print_board(lst)
    while True:
        if count % 2 == 0:
            make_move('X', lst)
        else:
            make_move('O', lst)
        count += 1
        if count > 4:
            check_winner = get_check_winner(lst)
            if check_winner:
                print_board(lst)
                print(f'The player who plays with "{check_winner}" wins! Congratulations!')
                break
        if count == 9:
            print_board(lst)
            print('Draw!')
            break
        print_board(lst)


while True:
    print()
    print('WELCOME TO THE TIC-TAC-TOE GAME!')
    print('Each cell has a number from 1 to 9. Enter the number to make a move...')
    fields = get_fields()
    play_game(fields)
    print()
    answer = input('Do you want to play again? (Y/N) ')
    if answer.lower() == 'y':
        continue
    else:
        break
