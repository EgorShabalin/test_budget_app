import unittest
import os
from datetime import datetime
from unittest.mock import patch
from io import StringIO
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
        data = find("Зарплата-ТЕСТ")
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
            id="10011",
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
        mock_obj = Budget_item(
            id="99999",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="1000",
            desc="Зарплата",
        )
        save(mock_obj)
        self.assertTrue(get_object("99999"))
        delete("99999")
        self.assertFalse(get_object("99999"))

    @patch("main.get_all_objects")
    def test_get_balance(self, mock_get_all_objects):
        mock_get_all_objects.return_value = [
            Budget_item(
                id="1000",
                date="2024-05-08 15:48:31.543158",
                cat="Доход",
                amount="1000",
                desc="Зарплата",
            ),
            Budget_item(
                id="1001",
                date="2024-05-08 15:48:31.543158",
                cat="Доход",
                amount="100",
                desc="Кешбек",
            ),
            Budget_item(
                id="1002",
                date="2024-05-08 15:48:31.543158",
                cat="Расход",
                amount="600",
                desc="Налог",
            ),
        ]
        result = get_balance()
        self.assertEqual(result, [1100, 600, 500])

    @patch("builtins.input", side_effect=["1000", "Пополнение-ТЕСТ"])
    def test_deposit(self, mock_input):
        deposit()
        self.assertEqual(
            find("Пополнение-ТЕСТ").pop().desc.rstrip(),
            Budget_item(
                id="0",
                date=datetime(2024, 5, 8, 15, 48, 31, 543158),
                cat="Доход",
                amount="1000",
                desc="Пополнение-ТЕСТ",
            ).desc,
        )

    def test_deposit_amount(self):
        amount = "222"
        description = "deposit_amount_test"
        deposit_amount(amount, description)
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            str_balance()
            result = find("deposit_amount_test").pop().desc.rstrip()
            output = fake_stdout.getvalue().strip()
            self.assertTrue("222" in output)
        self.assertEqual("deposit_amount_test", result.strip())

    @patch("builtins.input", side_effect=["1111", "Расход-ТЕСТ"])
    def test_withdraw(self, mock_input):
        withdraw()
        self.assertEqual(
            find("Расход-ТЕСТ").pop().amount.rstrip(),
            Budget_item(
                id="1111",
                date=datetime(2024, 5, 8, 15, 48, 31, 543158),
                cat="Расход",
                amount="1111",
                desc="Расход-ТЕСТ",
            ).amount,
        )

    def test_withdraw_amount(self):
        amount = "333"
        description = "withdraw_amount_test"
        withdraw_amount(amount, description)
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            str_balance()
            result = find("withdraw_amount_test").pop().desc.rstrip()
            output = fake_stdout.getvalue().strip()
            self.assertTrue("68667" in output)
        self.assertEqual("withdraw_amount_test", result.strip())

    def test_show_all(self):
        expected_result = read_file()
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            show_all()
            output = fake_stdout.getvalue().strip()
            self.assertTrue(output in expected_result)

        self.assertEqual(output, expected_result.strip())

    @patch("builtins.input", side_effect=["444444", "4", "Успешно Редактирование-ТЕСТ"])
    def test_edit_item(self, mock_input):
        mock_obj = Budget_item(
            id="444444",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="1000",
            desc="Редактирование-ТЕСТ",
        )
        save(mock_obj)
        self.assertTrue(get_object("444444"))
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            edit_item()
            self.assertTrue("Успешно" in get_object("444444").desc)
            output = fake_stdout.getvalue().strip()
            self.assertTrue("Данные Обновлены!" in output)

    @patch("builtins.input", side_effect=["121212"])
    def test_search(self, mock_input):
        mock_obj = Budget_item(
            id="121212",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="1000",
            desc="Поиск-ТЕСТ",
        )
        save(mock_obj)
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            search("Поиск")
            self.assertTrue("Поиск" in get_object("121212").desc)
            output = fake_stdout.getvalue().strip()
            self.assertTrue("121212" in output)

    @patch("builtins.input", side_effect=["Да"])
    def test_delete_item(self, mock_input):
        mock_obj = Budget_item(
            id="151515",
            date="2024-05-08 15:48:31.543158",
            cat="Доход",
            amount="1000",
            desc="Зарплата",
        )
        save(mock_obj)
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            delete_item("151515")
            output = fake_stdout.getvalue().strip()
            self.assertTrue("Удалена" in output and "151515" in output)
            self.assertFalse(get_object("151515"))


if __name__ == "__main__":
    unittest.main()
