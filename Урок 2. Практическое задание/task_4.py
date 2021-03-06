"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_row(n, num=1):
    """Функция рекурсивного расчета суммы ряда 1 -0.5 0.25 -0.125 ...

    :param n: Количество итераций
    :param num: Число итерации (по-умолчанию: 1)
    :return: Возвращает сумму ряда
    """
    if n <= 0:
        return 0
    print(f"{num}", end=" ")
    summa = num + sum_row(n - 1, -(num / 2))
    return summa


#################################################
try:
    nums = input("Введите количество итераций и стартовое число через пробел, либо только число итераций: ").split(' ')
    if len(nums) > 1:
        print(f"\nСумма: {sum_row(int(nums[0]), int(nums[1]))}")
    else:
        print(f"\nСумма: {sum_row(int(nums[0]))}")
except:
    print("Неверный ввод")
