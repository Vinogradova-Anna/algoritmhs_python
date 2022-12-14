"""Для каждой из трех функций выполнить следующее:
1) для каждого выражения вместо !!! укажите сложность.
1) для каждого выражения вместо символов !!! укажите сложность.
2) определите сложность алгоритма в целом (Сложность: !!!).
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- Сложность нужно указать только там, где есть !!!
-- Сложности встроенных функций нужно искать
    в таблицах (материалы к уроку).
-- Сложности встроенных функций и операций нужно искать
    в таблицах (см. материалы к уроку).
"""

import random
from random import sample


##############################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 1:
    Создать множество из списка
    Сложность: !!!.
    """
    lst_to_set = set(lst_obj)  # линейная О(n), время тем больше, чем больше массив
    return lst_to_set  # линейная О(n), время тем больше, чем больше массив
##############################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: !!!.
    """
    for j in range(len(lst_obj)):          # проход О(n)
        if lst_obj[j] in lst_obj[j+1:]:    # в этой строчке алгоритм линейно масштабируется, O(n) - линейная
            return False                   # в этой строчке алгоритм выдает результат вложенного цикла, O(n^2) - квадратичная
    return True                            # в этой строчке алгоритм выдает результат вложенного цикла, O(n^3) - кубическая
##############################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: !!!
    """
    lst_copy = list(lst_obj)                 # константная О(1), тк присвоение
    lst_copy.sort()                          # линейно-логарифмическая O(log n)
    for i in range(len(lst_obj) - 1):        # проход О(n)
        if lst_copy[i] == lst_copy[i+1]:     # проверка O((len(s)) зависит от длины аргумена, время тем больше чем больше массив - линейная О(n)
            return False                     # по мере вложенности растет и временная вложенность O(n^2)
    return True                              # в этой строчке алгоритм выдает результат вложенного цикла, O(n^3) - кубическая
for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)
    lst = sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))


