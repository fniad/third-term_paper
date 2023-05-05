import os
from utils.utils_ import load_operations

OPERATIONS_DATA_PATH = os.path.join('data/operations.json')


def get_the_last_five_transactions(path=OPERATIONS_DATA_PATH):
    operation_list = load_operations(OPERATIONS_DATA_PATH)

    five_transaction = ""

    for operation in operation_list[:5]:
        transaction = operation.get_result_operation()
        five_transaction += f"{transaction} \n\n"

    return five_transaction



