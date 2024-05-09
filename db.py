from utils import get_data
from model import Budget_item


# Собрать список всех объектов
def get_all_objects():
    items_list = []
    dict_list = get_data()
    if dict_list:
        for item in dict_list:
            id = item["ID"]
            date = item["Дата"]
            cat = item["Категория"]
            amount = item["Сумма"]
            desc = item["Описание"]
            obj = Budget_item(id, date, cat, amount, desc)
            items_list.append(obj)
        return items_list
    else:
        return None


# Получить объект по его id
def get_object(id):
    dict_list = get_data()
    for item in dict_list:
        if item["ID"] == str(id):
            id = item["ID"]
            date = item["Дата"]
            cat = item["Категория"]
            amount = item["Сумма"]
            desc = item["Описание"]
            obj = Budget_item(id, date, cat, amount, desc)
            return obj
        else:
            pass


# Поиск по аттрибутам объекта
def find(request):
    result = set()
    request = str(request).lower()
    objects = get_all_objects()
    for obj in objects:
        if request in str(obj.id):
            result.add(obj)
        if request in str(obj.date):
            result.add(obj)
        if request in str(obj.cat).lower():
            result.add(obj)
        if request in str(obj.amount):
            result.add(obj)
        if request in str(obj.desc).lower():
            result.add(obj)
    return result


# Назначить индекс для сохранения записи. Находит самое больщое число и прибавляет 1.
def get_index():
    index = 0
    objects = get_all_objects()
    if objects:
        for obj in objects:
            if int(obj.id) > index:
                index = int(obj.id)
            else:
                pass
        index += 1
        return str(index)
    else:
        return "1"


# Сохраняет запись в файл из объекта
def save(obj):
    file = "money.txt"
    with open(file, "a") as f:
        f.write(
            f"""
ID: {obj.id}
Дата: {obj.date}
Категория: {obj.cat}
Сумма: {obj.amount}
Описание: {obj.desc}            
"""
        )


# Принимает отредактированный объект, находит соответствие из имеющихся объектов по id, сохраняет изменения.
def edit(obj):
    objects = get_all_objects()
    for o in objects:
        if o.id == obj.id:
            o.date = obj.date
            o.cat = obj.cat
            o.amount = obj.amount
            o.desc = obj.desc
        else:
            pass
    file = "money.txt"
    with open(file, "w") as f:
        for ob in objects:
            f.write(
                f"""
ID: {ob.id}
Дата: {ob.date}
Категория: {ob.cat}
Сумма: {ob.amount}
Описание: {ob.desc}
"""
            )


# Создает список всех объектов, удаляет из него переданный в аттрибуте объект, сохраняет изменения.
def delete(obj):
    all_obj = get_all_objects()
    if obj in all_obj:
        all_obj.remove(obj)
    file = "money.txt"
    for o in all_obj:
        with open(file, "w") as f:
            f.write(
                f"""
ID: {o.id}
Дата: {o.date}
Категория: {o.cat}
Сумма: {o.amount}
Описание: {o.desc}
"""
            )
