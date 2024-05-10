# Чтение файла money.txt
def read_file():
    file = "money.txt"
    with open(file, "r") as f:
        data = f.read()
    # print(data)
    return data


# Представление содержимого файла money.txt в виде списка словарей
def get_data():
    result = []
    data = read_file()
    data = data.splitlines()
    data = [data[i + 1 : i + 6] for i in range(0, len(data), 6)]
    for item in data:
        dict = {}
        for i in item:
            k, v = i.split(": ")
            dict[k] = v.rstrip()
            if not dict in result:
                result.append(dict)
    # print(result)
    return result
