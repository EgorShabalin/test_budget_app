import argparse  # argparse парсер для обработки аргументов

from datetime import datetime  # библиотека для обработки даты и времени

# импорт функций и модели объекта
from db import get_all_objects, get_index, save, get_object, edit, find
from model import Budget_item


# инициализация argparse парсера
parser = argparse.ArgumentParser(
    prog="BUDGET MANAGER",
    description="Управляй своим бюджетом! Принимаются только целые числа!",
)

# Обработка аргументов
parser.add_argument(
    "-balance",
    dest="balance",
    action="store_true",
    help="Узнать текущий Баланс",
)
parser.add_argument(
    "-income",
    dest="income",
    action="store_true",
    help="Узнать весю сумму Дохода",
)
parser.add_argument(
    "-expenses",
    dest="expenses",
    action="store_true",
    help="Узнать всю сумму Расходов",
)
parser.add_argument(
    "-add",
    dest="add",
    action="store_true",
    help="Пополнить Баланс",
)
parser.add_argument(
    "-sub",
    dest="subtract",
    action="store_true",
    help="Израсходовать Сумму",
)
parser.add_argument(
    "-show",
    dest="show_all",
    action="store_true",
    help="Показать все Записи",
)
parser.add_argument(
    "-edit",
    dest="edit_item",
    action="store_true",
    help="Редактировать Запись",
)
parser.add_argument(
    "-search",
    dest="search",
    action="store_true",
    help="Поиск по всем Записям",
)
parser.add_argument(
    "-dep",
    nargs=2,
    metavar=("amount", "description"),
    help="Add an amount with description",
)
parser.add_argument(
    "-wtd",
    nargs=2,
    metavar=("amount", "description"),
    help="Add an amount with description",
)


# Передача аргументов в парсер
args = parser.parse_args()


# Функция подсчета баланса, возвращает только число
def get_balance():
    pos = []
    neg = []
    result = []
    objects = get_all_objects()
    for obj in objects:
        if obj.cat == "Доход":
            pos.append(int(obj.amount))
        else:
            neg.append(int(obj.amount))
    result.append(sum(pos))
    result.append(sum(neg))
    result.append(sum(pos) - sum(neg))
    return result


# Возвращает строку с Балансом
def str_balance():
    bal = get_balance()
    print(f"Ваш баланс: {bal[2]}")


# Возвращает строку с общим Доходом
def get_income():
    bal = get_balance()
    print(f"Ваш ощий Доход: {bal[0]}")


# Возвращает строку с общим Расходом
def get_expenses():
    bal = get_balance()
    print(f"Ваш ощий Расход: {bal[1]}")


# Ввод и сохранение записи о пополнение баланса
def deposit():
    amount = input("Сумма дохода: ")
    desc = input("Описание: ")
    id = get_index()
    date = datetime.now()
    cat = "Доход"
    obj = Budget_item(id, date, cat, amount, desc)
    save(obj)
    print(f"Ваш баланс пополнен на сумму {amount}.")
    str_balance()


def deposit_amount(amount, desc):
    id = get_index()
    date = datetime.now()
    cat = "Доход"
    obj = Budget_item(id, date, cat, amount, desc)
    save(obj)
    print(f"Ваш баланс пополнен на сумму {amount}.")
    str_balance()


# Ввод и сохранение записи о расходе
def withdraw():
    amount = input("Сумма расхода: ")
    bal = get_balance()
    if int(amount) > bal[2]:
        print("Недостаточно средств!")
    else:
        desc = input("Описание: ")
        id = get_index()
        date = datetime.now()
        cat = "Расход"
        obj = Budget_item(id, date, cat, amount, desc)
        save(obj)
        print(f"Израсходована сумма {amount}.")
        str_balance()


def withdraw_amount(amount, desc):
    bal = get_balance()
    if int(amount) > bal[2]:
        print("Недостаточно средств!")
    else:
        id = get_index()
        date = datetime.now()
        cat = "Расход"
        obj = Budget_item(id, date, cat, amount, desc)
        save(obj)
        print(f"Израсходована сумма {amount}.")
        str_balance()


# Показать все записи
def show_all():
    objects = get_all_objects()
    for obj in objects:
        print(
            f"""
ID: {obj.id}
Дата: {obj.date}
Категория: {obj.cat}
Сумма: {obj.amount}
Описание: {obj.desc}
"""
        )


# Редактирование записи по указанному id
def edit_item():
    show_all()
    item_id = input("Укажите ID записи для редактирования: ")
    obj = get_object(item_id)
    print(
        f"""
Вы выбрали эту запись:

ID: {obj.id}
Дата: {obj.date}
Категория: {obj.cat}
Сумма: {obj.amount}
Описание: {obj.desc}
"""
    )

    line_to_edit = input(
        """
Для редактирвания Даты введите 1
Для редактирвания Категории введите 2
Для редактирвания Суммы введите 3
Для редактирвания Описания введите 4
Ваш выбор: """
    )
    if line_to_edit == "1":
        obj.date = input("Введите новую Дату: ")
    elif line_to_edit == "2":
        print("Введите 1 - Доход или 2 - Расход")
        inp = input()
        if inp == "1":
            obj.cat = "Доход"
        elif inp == "2":
            obj.cat = "Расход"
        else:
            print("ОШИБКА: Вы ввели неверное число! Попробуйте еще раз!")
    elif line_to_edit == "3":
        obj.amount = input("Введите новую Сумму: ")
    elif line_to_edit == "4":
        obj.desc = input("Введите новую Описание: ")
    else:
        print("ОШИБКА: Вы ввели неверное число! Попробуйте еще раз!")

    edit(obj)
    print("Данные Обновлены!")


# Поиск по аттрибутам сохраненных объектов
def search():
    text = input("Введите информацию для поиска: ")
    result = find(text)
    if result:
        print("\nНайдены Записи:")
        print("================================")
        for i in result:

            print(f"ID: {i.id}")
            print(f"Дата: {i.date}")
            print(f"Категория: {i.cat}")
            print(f"Сумма: {i.amount}")
            print(f"Описание: {i.desc}")
            print("================================")
    else:
        print("По введенному запросу Записей не найдено...")


# Обработка введенных аттрибутов
if args.balance:
    str_balance()
elif args.income:
    get_income()
elif args.expenses:
    get_expenses()
elif args.add:
    deposit()
elif args.subtract:
    withdraw()
elif args.show_all:
    show_all()
elif args.edit_item:
    edit_item()
elif args.search:
    search()
elif args.dep:
    deposit_amount(args.dep[0], args.dep[1])
elif args.wtd:
    withdraw_amount(args.wtd[0], args.wtd[1])
else:
    print("Введите -h для получения справки.")
