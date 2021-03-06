"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from random import randint
from timeit import timeit
import math


def sort_1(lst):
    """
    Функция сортировки списка по убыванию стандартным алгоритмом пузырька

    :param lst: Исходный список
    :return: Отсортированный список
    """
    n, c = 1, 0
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            c += 1
        n += 1
    # print(f"Количество циклов: {c}")
    return lst


def sort_2(lst):
    """
    Функция сортировки списка по убыванию "улучшенным" алгоритмом пузырька

    :param lst: Исходный список
    :return: Отсортированный список
    """
    n, c = 1, 0
    while n < len(lst):
        changed = False
        for i in range(len(lst) - n):
            if i == 0:
                t1, t2 = lst[i:i+2]
                if t1 < t2:
                    lst[i], lst[i + 1] = t2, t1
                    changed = True
            else:
                t0, t1, t2 = lst[i-1:i+2]
                if t1 < t2:
                    if t0 < t2:
                        lst[i - 1], lst[i], lst[i + 1] = t2, t0, t1
                    else:
                        lst[i], lst[i + 1] = t2, t1
                    changed = True
            c += 1
        n += 1
        if not changed:
            break
    # print(f"Количество циклов: {c}")
    return lst


def my_sort_shella(lst):
    """
    Функция сортировки списка по убыванию алгоритмом Шелла.
    Сам по себе алгоритм не дал однозначного результата, иногда появляляась ошибка,
    по-этому дополнен алгшоритмом пузырька.

    :param lst: Исходный список
    :return: Отсортированный список
    """
    c = 0
    step = (len(lst) * 3) // 4
    while step > 0:
        for i in range(len(lst) - 1):
            j = i + step
            if j > len(lst) - 1:
                break
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            c += 1
        step = (step * 3) // 4
    n = 1
    while n < len(lst):
        changed = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                changed = True
            c += 1
        if not changed:
            break
        n += 1
    # print(f"Количество циклов: {c}")
    return lst


# Генерация списка
source_list = [randint(-100, 100) for _ in range(50)]
# Вывод исходного списка
print(source_list)

# Сортировка списка стандартным алгоритмом
sorted_list_1 = sort_1(source_list[:])
# Вывод получившегося списка
print(sorted_list_1)

# Сортировка списка "улучшенным" алгоритмом
sorted_list_2 = sort_2(source_list[:])
# Вывод получившегося списка
print(sorted_list_2)

# Сортировка списка алгоритмом Шелла, дополненным в завершении пузырьком
sorted_list_3 = my_sort_shella(source_list[:])
# Вывод получившегося списка
print(sorted_list_3)

# Сортировка списка алгоритмом Шелла, дополненным в завершении пузырьком
sorted_list_4 = sorted(source_list[:], reverse=True)
# Вывод получившегося списка
print(sorted_list_4)

# Замеры
print(f"Замер func_1(): {timeit('sort_1(source_list[:])', 'from __main__ import sort_1, source_list', number=1000)}")
# >>> Замер func_1(): 0.49898629999999994
print(f"Замер func_2(): {timeit('sort_2(source_list[:])', 'from __main__ import sort_2, source_list', number=1000)}")
# >>> Замер func_2(): 0.45766620000000013
print(f"Замер my_sort_shella(): {timeit('my_sort_shella(source_list[:])', 'from __main__ import my_sort_shella, source_list', number=1000)}")
# >>> Замер my_sort_shella(): 0.19445409999999996
print(f"Замер sorted(): {timeit('sorted(source_list[:], reverse=True)', 'from __main__ import source_list', number=1000)}")
# >>> Замер sorted(): 0.002799300000000171

"""
Ускорение по сортировке наблюдается неплохое.

Оптимизацию и улучшение алгоритма сортировки пузырьком делал в 3-х направлениях:
1. Добавил флаг, который обозначает что сортировка далее не ребуется. Т.е. если при обходе списка
    в поисках возможных изменений не было перестановок, то осуществляется досрочный выход из цикла.
    Данный метод экономит совсем немного, количество итераций сокращается максимум на несколько циклов.
    (в списке из 50 чисел от -100 до 100: ~1225 циклов сократилось до ~1223)
2. Добавил в цикл перестановку с предыдущим элементов, кроме следущего.
    Это позволило существенно сократить количество циклов.
    (в списке из 50 чисел от -100 до 100: ~1225 циклов сократилось до ~900)
3. Добавишл в цикл хранение значений проверяемых элементов во временные переменные,
    т.к. сложность обращение к элементам списка зависит от длины списка,
    а обращений к элементам в исходном состоянии много.

Алгоритм Шелла сам по себе не дает однозначного решгения, с подбором шага запутался.
По-этому дополнил алгоритм Шелла алгоритмом пузырька в завершении.
Количество итераций сокротилось до ~465
"""
