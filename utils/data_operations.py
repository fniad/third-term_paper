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


