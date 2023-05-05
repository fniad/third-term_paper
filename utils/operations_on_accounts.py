from utils.load_json_util import load_operations


def get_the_last_five_transactions(path):
    operation_list = load_operations(path)

    five_transaction = ""

    for operation in operation_list[:5]:
        transaction = operation.get_result_operation()
        five_transaction += f"{transaction}\n\n"

    return five_transaction
