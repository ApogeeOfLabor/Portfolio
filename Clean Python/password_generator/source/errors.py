import sys


def check_entered_data(entered_data):
    if entered_data.lower() == 'simple' or (entered_data.isdigit() and entered_data in [str(num) for num in range(4, 8)]):
        return 'simple'
    elif entered_data.lower() == 'medium' or (entered_data.isdigit() and entered_data in [str(num) for num in range(8, 12)]):
        return 'medium'
    elif entered_data.lower() == 'hard' or (entered_data.isdigit() and entered_data in [str(num) for num in range(12, 19)]):
        return 'hard'


def correcting_entered_data(min_char, max_char):
    if input(f'The length of a simple password is in the range from {min_char} to {max_char} characters.\nDo you '
             f'want to repeat the data entry? ("yes" or "no"): ').lower() == "yes":
        return 1
    else:
        sys.exit()


def value_error(func):
    print('Incorrect data entry')
    if input('Do you want to repeat the data entry? ("yes" or "no"): ') == "yes":
        return func()
    else:
        sys.exit()
