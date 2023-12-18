"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [el**2 for el in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """

    def FilterFunc(n):
        return (filter_type == ODD and n % 2 == 1) or \
               (filter_type == EVEN and n % 2 == 0) or \
               (filter_type == PRIME and is_prime(n))

    # filter solution
    filter_solution = list(
        filter(
            lambda n: FilterFunc(n),
            numbers,
    ))
    # list comprehension solution
    list_comp_result = [n for n in numbers if FilterFunc(n)]
    assert list_comp_result == filter_solution
    return filter_solution
