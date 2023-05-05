from utils.utils_mask import get_mask_account, get_mask_card


class Operation:
    """ Класс операции """
    def __init__(self, data_operation, description_operation, info_from_operation, info_to_operation, amount_operation,
                 currency_operation):
        """ Устанавливает необходимые атрибуты операции """
        self.data_operation = data_operation
        self.description_operation = description_operation
        self.info_from_operation = info_from_operation
        self.info_to_operation = info_to_operation
        self.amount_operation = amount_operation
        self.currency_operation = currency_operation

    def get_normal_format_data(self):
        """ Вывод даты в формате dd.mm.gggg """
        return f'{self.data_operation[8:10]}.{self.data_operation[5:7]}.{self.data_operation[:4]}'

    def get_type_to(self):
        """ Выводит замаскированный номер счёта или карты, от кого операция"""
        if self.info_to_operation.startswith('Счет'):
            return get_mask_account(self.info_to_operation)
        else:
            return get_mask_card(self.info_to_operation)

    def get_type_from(self):
        """ Выводит замаскированный номер счёта или карты, от кому операция"""
        try:
            if self.info_from_operation.startswith('Счет'):
                return get_mask_account(self.info_from_operation)
            else:
                return get_mask_card(self.info_from_operation)
        except AttributeError:
            return 'Неизвестно'

    def get_result_operation(self):
        """ Вывод описания по каждой операции в запрошеном виде """
        return f'{self.get_normal_format_data()} {self.description_operation} \n' \
               f'{self.get_type_from()} -> {self.get_type_to()} \n' \
               f'{self.amount_operation} {self.currency_operation}'

    def __repr__(self):
        """ Для отладки: выводит операцию и её свойства """
        return f'{self.__class__.__name__}(' \
               f'data="{self.data_operation}", ' \
               f'description={self.description_operation}, ' \
               f'info_from="{self.info_from_operation}" ' \
               f'info_to="{self.info_to_operation}" ' \
               f'amount="{self.amount_operation}" ' \
               f'currency="{self.currency_operation}" ' \
               f')'
