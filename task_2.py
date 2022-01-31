"""Задание 2.
ПО для вендингового аппарата.
Язык программирования Python"""

BANKNOTE_TYPES = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000][::-1]


def banknotes_from_change(change):
    res = ""
    for banknote in BANKNOTE_TYPES:
        count = change // banknote
        if count != 0:
            res += f"{banknote} руб: {count} шт.,"
            change -= count * banknote
    return res[:-1]


order_sum = int(input("Сумма заказа:"))
client_sum = int(input("Внесённая сумма клиентом:"))
change_result = client_sum - order_sum
if change_result < 0:
    print(f"Недостаточно {abs(change_result)}р.")
elif change_result == 0:
    print("Сдачи нет")
else:
    print(banknotes_from_change(change_result))
