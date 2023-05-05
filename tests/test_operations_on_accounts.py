import os
import pytest
from utils.operations_on_accounts import get_the_last_five_transactions

DATA_TXT_RESULT = os.path.join('data/result_last_5_operations.txt')
OPERATIONS_DATA_PATH = os.path.join('data/operations.json')


@pytest.fixture()
def data_path():
    data_path_str = OPERATIONS_DATA_PATH
    return data_path_str


@pytest.fixture()
def data_result_txt():
    data_txt_result_path = DATA_TXT_RESULT
    return data_txt_result_path


@pytest.fixture()
def data_path_result_txt(data_result_txt):
    with open(data_result_txt, "r", encoding="utf-8") as f:
        expected_result = f.read()
    return expected_result


def test_get_the_last_five_transactions(data_path, data_path_result_txt):
    assert get_the_last_five_transactions(data_path) == data_path_result_txt
