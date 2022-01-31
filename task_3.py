"""Задание 3.
Заказы на линзы.
Язык программирования Python."""

cyclops_num = int(input('Введите количество циклопов:'))
list_dioptria = [int(input("Введите диоптрии по 1:")) for _ in range(cyclops_num)]
list_dioptria.sort()
count = 0
index = 1
while index < len(list_dioptria):
    if abs(list_dioptria[index - 1] - (list_dioptria[index])) < 3:
        count += 1
        index += 2
    else:
        index += 1
print(list_dioptria)
print(f'Количество пар = {count + (len(list_dioptria) - 2 * count)}')
