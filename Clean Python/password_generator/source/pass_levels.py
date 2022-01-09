import gen_list_chars
import errors


def get_len(min_char, max_char, func):
    try:
        return int(input(f'Set the password length ({min_char}-{max_char} characters): '))
    except ValueError:
        return errors.value_error(func)


def simple():
    min_char, max_char = 4, 7
    try:
        len_pass = get_len(min_char, max_char, simple)
        if 4 <= len_pass < 6:
            return gen_list_chars.add_chars(len_pass - 1, 1)
        elif len_pass == 6:
            return gen_list_chars.add_chars(len_pass - 2, 2)
        elif len_pass == 7:
            return gen_list_chars.add_chars(len_pass - 3, 2, 1)
        else:
            if errors.correcting_entered_data(min_char, max_char):
                return simple()
    except ValueError:
        return errors.value_error(simple)


def medium():
    min_char, max_char = 8, 11
    try:
        len_pass = get_len(min_char, max_char, medium)
        if len_pass == 8:
            return gen_list_chars.add_chars(len_pass - 4, 2, 2)
        elif 8 < len_pass <= 11:
            return gen_list_chars.add_chars(len_pass - 5, 2, 2, 1)
        else:
            if errors.correcting_entered_data(min_char, max_char):
                return medium()
    except ValueError:
        return errors.value_error(medium)


def hard():
    min_char, max_char = 12, 18
    try:
        len_pass = get_len(min_char, max_char, hard)
        if 12 <= len_pass < 15:
            return gen_list_chars.add_chars(len_pass - 6, 2, 2, 2)
        elif 15 <= len_pass < 17:
            return gen_list_chars.add_chars(len_pass - 7, 2, 3, 2)
        elif 17 <= len_pass <= 18:
            return gen_list_chars.add_chars(len_pass - 8, 3, 2, 3)
        else:
            if errors.correcting_entered_data(min_char, max_char):
                return hard()
    except ValueError:
        return errors.value_error(medium)

        
if __name__ == '__main__':
    print(simple(), medium(), hard(), sep='\n')
