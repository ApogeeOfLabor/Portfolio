def get_sum_numbers_multiples_of_seven(list_num):

    """ Сортировка чисел сумма цифр которых кратна семи """

    return sum([number for number in list_num if sum([int(item) for item in iter(str(number))]) % 7 == 0])


if __name__ == '__main__':
    odd_numbers_list = [num ** 3 for num in range(1, 1000, 2)]

    #  section A:
    print(f"result: {get_sum_numbers_multiples_of_seven(odd_numbers_list)}, id: {id(odd_numbers_list)}")

    #  section B - создаётся новый объект в памяти.
    modify_odd_numbers_list = [item + 17 for item in odd_numbers_list]
    print(f"result: {get_sum_numbers_multiples_of_seven(modify_odd_numbers_list)}, id: {id(modify_odd_numbers_list)}")

    #  section C - без создания нового объекта.
    for index, value in enumerate(odd_numbers_list):
        odd_numbers_list[index] = value + 17
    print(f"result: {get_sum_numbers_multiples_of_seven(odd_numbers_list)}, id: {id(odd_numbers_list)}")
