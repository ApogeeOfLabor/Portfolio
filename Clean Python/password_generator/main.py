from source import errors
from source import data
from source import pass_levels
import eel

eel.init("assets")
eel.start("index.html", size=(600, 400))


@eel.expose
def start_hello():
    return data.start_hello


@eel.expose
def start():
    try:
        entered_difficulty_level = input().lower()
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


# if __name__ == '__main__':
#     print(f'Your password: {start()}')
