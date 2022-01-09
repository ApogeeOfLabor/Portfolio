from source import errors
from source import data
from source import pass_levels
import eel


def start():
    try:
        entered_difficulty_level = input(data.start_hello).lower()
        if pass_levels.simple.__name__ == errors.check_entered_data(entered_difficulty_level):
            return pass_levels.simple()
        if pass_levels.medium.__name__ == errors.check_entered_data(entered_difficulty_level):
            return pass_levels.medium()
        if pass_levels.hard.__name__ == errors.check_entered_data(entered_difficulty_level):
            return pass_levels.hard()
        else:
            raise ValueError
    except ValueError:
        return errors.value_error(start)


if __name__ == '__main__':
    print(f'Your password: {start()}')