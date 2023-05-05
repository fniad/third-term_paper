import os
from utils.operations_on_accounts import get_the_last_five_transactions

OPERATIONS_DATA_PATH = os.path.join('data/operations.json')

print(get_the_last_five_transactions(OPERATIONS_DATA_PATH))

