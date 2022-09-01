"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""

class StackClass:
    def __init__(self, size_m):
        self.elems = []
        self.size_m = size_m

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]] # пока что 1 пустой массив, если по условию будет нужно, добавим еще

    def push_in(self, elem):
        """Предполагаем, что верхний эл-т стека находится в конце списка, если размер > size_m, то вставляем новый массив"""
        if len(self.elems[len(self.elems) - 1]) < len(self.size_m):
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([]) #иначе доюавляем массив
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        """Если крайняя стопка пустая, то удалим её"""
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        elem_count = 0
        for i in self.elems:
            elem_count += len(i)
        return elem_count

    def stack_count(self):
        return len(self.elems)

# наполняем стек
if __name__ == '__main__':
    plate = StackClass(2)
    print(type(plate))
    plate.push_in('p1')
    plate.push_in('p2')
    plate.push_in('p3')
    plate.push_in('p4')
    print(plate)
    # получаем значение первого элемента с вершины, но не удаляем сам элемент
    print(plate.get_val())
    # убираем элемент с вершины
    print(plate.pop_out())
    # узнаем размер стека
    print(plate.stack_size())
    # узнаем количество стоек
    print(plate.stack_count())
    print(plate)

