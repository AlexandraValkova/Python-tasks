import random

#сортировка по вставкам
def sort_by_inserts(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int

#бинарный поиск
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


numbers_string = input("Введите последовательность чисел через пробел: ")

element = int(input("Введите любое число из ранее введеных: "))

numbers_list = list(map(int, numbers_string.split(sep=" ")))

sequence_sorted = sort_by_inserts(numbers_list)
print("Отсортированные числа по возрастанию: ", sequence_sorted)

element_index = binary_search(sequence_sorted, element, 0, len(sequence_sorted))

print("Индекс элемента  из отсортированнного списка: ", element_index)
