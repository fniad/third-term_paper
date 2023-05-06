import os
from utils.operations_on_accounts import get_the_last_five_transactions

OPERATIONS_DATA_PATH = os.path.join('data/operations.json')


def main():
    print(get_the_last_five_transactions(OPERATIONS_DATA_PATH))


if __name__ == '__main__':
    main()
