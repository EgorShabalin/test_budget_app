import unittest
from unittest import mock
from utils import *
from db import *
from main import *


class TestBudget(unittest.TestCase):
    def test_read_file(self):
        data = read_file()
        self.assertEqual(
            data[:186],
            """
ID: 1
Дата: 2024-05-08 15:48:31.543158
Категория: Доход
Сумма: 35000
Описание: Зарплата            

ID: 2
Дата: 2024-05-08 15:48:47.745124
Категория: Расход
Сумма: 1500
Описание: Ужин
""",
        )

    def test_get_data(self):
        data = get_data()
        self.assertEqual(
            data[:2],
            [
                {
                    "ID": "1",
                    "Дата": "2024-05-08 15:48:31.543158",
                    "Категория": "Доход",
                    "Сумма": "35000",
                    "Описание": "Зарплата            ",
                },
                {
                    "ID": "2",
                    "Дата": "2024-05-08 15:48:47.745124",
                    "Категория": "Расход",
                    "Сумма": "1500",
                    "Описание": "Ужин",
                },
            ],
        )

    def test_get_all_objects(self):
        data = get_all_objects()
        item_1 = Budget_item(
            id="1",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="35000",
            desc="Зарплата            ",
        )
        item_2 = Budget_item(
            id="2",
            date="2024-05-08 15:48:47.745124",
            cat="Расход",
            amount="1500",
            desc="Ужин",
        )
        mock_data = [item_1, item_2]
        self.assertEqual(data[0].date, mock_data[0].date)

    def test_get_object(self):
        data = get_object("1")
        item_1 = Budget_item(
            id="1",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="35000",
            desc="Зарплата            ",
        )
        self.assertEqual(data.date, item_1.date)

    def test_find(self):
        data = find("плата")
        data = data.pop()
        result = {
            Budget_item(
                id="1",
                date="2024-05-08 15:48:31.543158",
                cat="Доход",
                amount="35000",
                desc="Зарплата            ",
            )
        }
        result = result.pop()
        self.assertEqual(data.date, result.date)


if __name__ == "__main__":
    unittest.main()
