import json
import os

from data.operations import Operation


def load_data(path):
    """Загружает данные из файла json"""
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_operations(path):
    """Создаёт список с экземплярами класса Операций и сортирует его по дате"""
    # список всех операций в формате словарей с ключами data, description, from, to
    operation_data = load_data(path)

    if operation_data is None:
        return []

    # список операций
    list_operation = []

    for operation in operation_data:
        if not operation:  # проверяем, что словарь не пустой
            continue
        try:
            operation = Operation(
                data_operation=operation.get('date'),
                description_operation=operation.get("description"),
                info_from_operation=operation.get('from', None),
                info_to_operation=operation.get("to"),
                amount_operation=operation.get("operationAmount").get("amount"),
                currency_operation=operation.get("operationAmount").get("currency").get("name"),
            )
        except KeyError:
            del operation
        else:
            list_operation.append(operation)

    sorted_operation = sorted(list_operation, key=lambda Operation: Operation.data_operation, reverse=True)
    return sorted_operation



