# Функция для сортировки списка
def sort_list(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

# Функция для двоичного поиска
def binary_search(list, number):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == number:
            return mid
        elif list[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Ввод последовательности чисел
input_string = input("Введите последовательность чисел через пробел: ")
try:
    input_list = [int(i) for i in input_string.split()]
except ValueError:
    print("Ошибка: введены некорректные данные")
else:
    # Проверка на соответствие условию ввода данных
    if len(input_list) < 2:
        print("Ошибка: введена последовательность слишком малого размера")
    else:
        # Ввод числа, с которым будем сравнивать элементы списка
        number = input("Введите любое число: ")
        try:
            number = int(number)
        except ValueError:
            print("Ошибка: введено некорректное число")
        else:
            # Сортировка списка и вывод отсортированного списка
            sorted_list = sort_list(input_list)
            print("Отсортированный список:", sorted_list)
            # Поиск позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу
            position = binary_search(sorted_list, number)
            if position == -1:
                print("В списке нет элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу")
            else:
                print("Позиция элемента:", position)