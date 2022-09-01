"""
Задание 3.
Для этой задачи:
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
"""
########
dict_companies = {'apple' : 10000,
                  'acer' : 1569,
                  'asus' : 5687,
                  'microsoft' : 15036,
                  'banana' : 9999,
                  'cucumber' : 4500,
                  'samsung' : 19000,
                  'xiomi' : 12000,
                  'htc': 6548,
                  'dell' : 8994}          # в этой строчке алгоритм линейно масштабируется, O(n) - линейная

max_elem = max(dict_companies.values())   # dict_companies.values() - O(1), если берем в целом выражение max_elem = max(dict_companies.values()) - O(n) - линейная
print("1 Max element of a dict: ", max_elem)


########
def large(arr):
    max_ = arr[0]                         # линейная О(n),
    for ele in arr:                       # проход О(n)
        if ele > max_:                    # в этой строчке алгоритм линейно масштабируется, O(n) - линейная
            max_ = ele                    # линейная О(n),
        return max_                       # в этой строчке алгоритм выдает результат вложенного цикла, O(n^2) - квадратичная

sorted_values = sorted(dict_companies.values())   # линейно-логарифмическая O(log n)
result = large(sorted_values)
print(result)
print(sorted_values)





