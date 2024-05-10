import unittest
from time import sleep
from unittest import mock
from utils import *
from db import *
from main import *


class TestBudget(unittest.TestCase):

    global data_safe
    data_safe = read_file()

    maxDiff = None

    def setUp(self):
        file = "money.txt"
        with open(file, "a") as f:
            f.write(
                f"""
ID: 1000
Дата: 2024-05-08 15:48:31.543158
Категория: Доход
Сумма: 35000
Описание: Зарплата-ТЕСТ
"""
            )

    def tearDown(self):
        file = "money.txt"
        with open(file, "w") as f:
            f.write(data_safe)

    def test_read_file(self):
        data = read_file()
        self.assertEqual(
            data[-97:],
            """
ID: 1000
Дата: 2024-05-08 15:48:31.543158
Категория: Доход
Сумма: 35000
Описание: Зарплата-ТЕСТ
""",
        )

    def test_get_data(self):
        data = get_data()
        self.assertEqual(
            data[-1],
            {
                "ID": "1000",
                "Дата": "2024-05-08 15:48:31.543158",
                "Категория": "Доход",
                "Сумма": "35000",
                "Описание": "Зарплата-ТЕСТ",
            },
        )

    def test_get_all_objects(self):
        data = get_all_objects()
        item_1 = Budget_item(
            id="1000",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="35000",
            desc="Зарплата-ТЕСТ",
        )
        mock_data = [item_1]
        self.assertEqual(data[-1].date, mock_data[0].date)

    def test_get_object(self):
        data = get_object("1000")
        item_1 = Budget_item(
            id="1000",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="35000",
            desc="Зарплата-ТЕСТ",
        )
        self.assertEqual(data.date, item_1.date)

    def test_find(self):
        data = find("-ТЕСТ")
        data = data.pop()
        result = {
            Budget_item(
                id="1000",
                date="2024-05-08 15:48:31.543158",
                cat="Доход",
                amount="35000",
                desc="Зарплата-ТЕСТ",
            )
        }
        result = result.pop()
        self.assertEqual(data.date, result.date)

    def test_get_index(self):
        index = get_index()
        data = get_data()
        num = 0
        for d in data:
            if int(d["ID"]) > num:
                num = int(d["ID"])
        num += 1

        self.assertEqual(index, str(num))

    def test_save(self):
        obj = Budget_item(
            id="1001",
            date="2024-05-08 15:48:31.543158",
            cat="cat-TEST",
            amount="am-TEST",
            desc="desc-TEST",
        )
        save(obj)
        result = get_object(obj.id)
        self.assertEqual(
            (
                obj.id,
                obj.date,
                obj.cat,
                obj.amount,
                obj.desc,
            ),
            (
                result.id,
                result.date,
                result.cat,
                result.amount,
                result.desc,
            ),
        )

    def test_edit(self):
        obj1 = Budget_item(
            id="1999",
            date="2024-05-08 15:48:31.543158",
            cat="cat-TEST",
            amount="am-TEST",
            desc="desc-TEST",
        )
        obj2 = Budget_item(
            id="1999",
            date="2222-05-08 15:48:31.543158",
            cat="category-TEST",
            amount="amount-TEST",
            desc="description-TEST",
        )
        save(obj1)
        edit(obj2)
        obj = get_object("1999")
        self.assertEqual(
            (
                obj2.id,
                obj2.date,
                obj2.cat,
                obj2.amount,
                obj2.desc,
            ),
            (
                obj.id,
                obj.date,
                obj.cat,
                obj.amount,
                obj.desc,
            ),
        )

    def test_delete(self):
        data = read_file()
        delete("1001")
        result = read_file()
        self.assertEqual(data, result)


if __name__ == "__main__":
    unittest.main()
