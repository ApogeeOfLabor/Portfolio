import random

up_chars = [chr(item) for item in range(ord('A'), ord('Z') + 1)]
low_chars = [chr(item) for item in range(ord('a'), ord('z') + 1)]
other_symbols = '! # $ % & " * + , - . / : ; < = > ? @ ^ _` ~ '.split()
num_chars = list(map(str, range(0, 10)))


def add_chars(len_low, len_up, len_num=0, len_other_symbols=0):
    if len_other_symbols:
        password_ = [random.choice(low_chars) for _ in range(len_low)]
        password_.extend([random.choice(up_chars) for _ in range(len_up)])
        password_.extend([random.choice(num_chars) for _ in range(len_num)])
        password_.extend([random.choice(other_symbols) for _ in range(len_other_symbols)])
        random.shuffle(password_)
        return ''.join(password_)
    elif len_num:
        password_ = [random.choice(low_chars) for _ in range(len_low)]
        password_.extend([random.choice(up_chars) for _ in range(len_up)])
        password_.extend([random.choice(num_chars) for _ in range(len_num)])
        random.shuffle(password_)
        return ''.join(password_)
    elif not len_num and not len_other_symbols:
        password_ = [random.choice(low_chars) for _ in range(len_low)]
        password_.extend([random.choice(up_chars) for _ in range(len_up)])
        random.shuffle(password_)
        return ''.join(password_)
