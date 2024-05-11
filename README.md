# BUDGET MANAGER - Личный финансовый кошелек

## Установка
Для работы с приложением необходимо создать или выбрать директорию, открыть ее в терминале и выполнить следующую команду:

Если установлен Git:

```
git pull https://github.com/EgorShabalin/test_budget_app.git
```

После чего все файлы приложения скопируются в указанную папку.

Или скачать zip со всеми файлами по ссылке:
<https://github.com/EgorShabalin/test_budget_app/archive/refs/heads/main.zip>

И распаковать в нужную папку.



## Запуск
Для запуска и использования приложения необходимо потребуется выполнение следующих команд:

#### Для просмотра встроенной справки:

```
$ python3 main.py -h

usage: BUDGET MANAGER [-h] [-balance] [-income] [-expenses] [-add] [-sub] [-show] [-edit] [-search] [-dep amount description]
                      [-wtd amount description] [-delete id]

Управляй своим бюджетом! Принимаются только целые числа!

optional arguments:
  -h, --help            show this help message and exit
  -balance              Узнать текущий Баланс
  -income               Узнать весю сумму Дохода
  -expenses             Узнать всю сумму Расходов
  -add                  Пополнить Баланс
  -sub                  Израсходовать Сумму
  -show                 Показать все Записи
  -edit                 Редактировать Запись
  -search               Поиск по всем Записям
  -dep amount description
                        Принимает 2 аргумента для записи Дохода: Сумма, Описание
  -wtd amount description
                        Принимает 2 аргумента для записи Расхода: Сумма, Описание
  -delete id            Принимает 1 аргумент для Удаления записи: Номер Записи
```

#### Для отображения доступного баланса:

Введите команду `-balance`

```
$ python3 main.py -balance

Ваш баланс: 29000
```

#### Для отображения общей суммы доходов:

Введите команду `-income`

```
$ python3 main.py -income

Ваш ощий Доход: 30600
```

#### Для отображения общей суммы расходов:

Введите команду `-expenses`

```
$ python3 main.py -expenses

Ваш ощий Расход: 1600
```

#### Для добавления записи о пополнении баланса:

Введите команду `-add`

```
$ python3 main.py -add

Сумма дохода: 100
Описание: Cashback
Ваш баланс пополнен на сумму 100.
Ваш баланс: 29100
```

Также можно использовать команду `-dep` с дополнительными аргументами суммы и описания записи: `-dep 100 'Cashback'`

```
$ python3 main.py -dep 100 'Cashback'

Ваш баланс пополнен на сумму 100.
Ваш баланс: 34100
```

#### Для ввода запииси о расходе:

Введите команду `-sub`

```
$ python3 main.py -sub

Сумма расхода: 100
Описание: Gum    
Израсходована сумма 100.
Ваш баланс: 29000
```

Также можно использовать команду `-wtd` с дополнительными аргументами суммы и описания записи: `-wtd 100 'Cellphone pay'`

```
$ python3 main.py -wtd 100 'Cellphone pay'

Израсходована сумма 100.
Ваш баланс: 34000
```

#### Для отображения всех записей:

Введите команду `-show`

```
$ python3 main.py -show

ID: 1
Дата: 2024-05-08 15:48:31.543158
Категория: Доход
Сумма: 30000
Описание: Зарплата            


ID: 2
Дата: 2024-05-08 15:48:47.745124
Категория: Расход
Сумма: 1500
Описание: Ужин
```

#### Для выбора и редактирования записи:

Введите команду `-edit`

```
$ python3 main.py -edit

ID: 1
Дата: 2024-05-08 15:48:31.543158
Категория: Доход
Сумма: 30000
Описание: Зарплата            


ID: 2
Дата: 2024-05-08 15:48:47.745124
Категория: Расход
Сумма: 1500
Описание: Ужин


Укажите ID записи для редактирования: 1

Вы выбрали эту запись:

ID: 1
Дата: 2024-05-08 15:48:31.543158
Категория: Доход
Сумма: 30000
Описание: Зарплата            


Для редактирвания Даты введите 1
Для редактирвания Категории введите 2
Для редактирвания Суммы введите 3
Для редактирвания Описания введите 4
Ваш выбор: 3
Введите новую Сумму: 35000
Данные Обновлены!
```

#### Для поиска по всем записям:

Введите команду `-search` и искомый текст в кавычках :`-search 'hot'`

```
$ python3 main.py -search 'hot'

Найдены Записи:
================================
ID: 4
Дата: 2024-05-08 15:51:27.989272
Категория: Расход
Сумма: 100
Описание: Hotdog
================================
```
#### Для удаления записи по ее номеру:

Введите команду `-delete` и номер записи для удаления: `-delete 8`

```
$ python3 main.py -delete 8

Удалить запись?

ID: 8
Дата: 2024-05-09 11:10:56.306038
Категория: Расход
Сумма: 100
Описание: Cellphone pay

Введите "Да" или "Нет": Да
Запись номер 8 была Удалена!
```

#### Для остановки приложения в любой момент нажмите сочетание клавиш:

```
Ctrl + C
```
<br>
<br>
<br>


## Задание

### Основные возможности:
- [x] 1. Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
- [x] 2. Добавление записи: Возможность добавления новой записи о доходе или расходе.
- [x] 3. Редактирование записи: Изменение существующих записей о доходах и расходах.
- [x] 4. Поиск по записям: Поиск записей по категории, дате или сумме.

### Требования к программе:
- [x] 1. Интерфейс: Реализация через консоль (CLI), без использования веб- или графического интерфейса (также без использования фреймворков таких как Django, FastAPI, Flask  и тд).
- [x] 2. Хранение данных: Данные должны храниться в текстовом файле. Формат файла определяется разработчиком.
- [x] 3. Информация в записях: Каждая запись должна содержать дату, категорию (доход/расход), сумму, описание (возможны дополнительные поля).

### Будет плюсом:
- [x] 1. Аннотации: Аннотирование функций и переменных в коде.
- [ ] 2. Документация: Наличие документации к функциям и основным блокам кода.
- [x] 3. Описание функционала: Подробное описание функционала приложения в README файле.
- [x] 4. GitHub: Размещение кода программы и примера файла с данными на GitHub.
- [x] 5. Тестирование.
- [x] 6. Объектно-ориентированный подход программирования.
