import pytest
import os
from utils.load_json_util import load_data, load_operations
from utils.operations_on_accounts import get_the_last_five_transactions

OPERATIONS_DATA_PATH = os.path.join('data/operations.json')
FOR_SIX_OPERATION_TEST = os.path.join('data/for_test_six_operations')


@pytest.fixture
def data_path():
    path_data = OPERATIONS_DATA_PATH
    return path_data


@pytest.fixture()
def data_path_2():
    path_data_2 = FOR_SIX_OPERATION_TEST
    return path_data_2


def test_get_the_last_five_transactions(data_path, data_path_2):
    five_operation = get_the_last_five_transactions(data_path)
    five_operation_2 = get_the_last_five_transactions(data_path_2)
    assert isinstance(five_operation, str)
    assert isinstance(five_operation_2, str)


def test_load_operations(data_path, data_path_2):
    sorted_operation = load_operations(data_path)
    sorted_operation_2 = load_operations(data_path_2)
    assert isinstance(sorted_operation, list)
    assert isinstance(sorted_operation_2, list)
