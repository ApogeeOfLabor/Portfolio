def get_time_interval(sec, templates):
    result = list()
    for key, value in templates.items():
        result.append(f"{sec // value} {key}" if sec // value else '')
        sec -= value * (sec // value)

    return result


if __name__ == '__main__':
    dict_templates = {
        'нед.': 604800,
        'дн.': 86400,
        'час.': 3600,
        'мин.': 60,
        'сек.': 1,
    }
    try:
        print(*get_time_interval(int(input('Введите колличество секунд: ')), dict_templates))
    except ValueError:
        print('Введено неверное значение!')
