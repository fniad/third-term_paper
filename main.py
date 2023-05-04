import os
from utils.utils import load_operations

OPERATIONS_DATA_PATH = os.path.join('data/operations.json')

print(load_operations(OPERATIONS_DATA_PATH))
