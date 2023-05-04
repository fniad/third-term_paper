class Operation:

    """Класс операции"""

    def __init__(self, data_operation, description_operation, info_from_operation, info_to_operation, amount_operation, currency_operation):

        """Устанавливает необходимые атрибуты операции"""

        self.data_operation = data_operation
        self.description_operation = description_operation
        self.info_from_operation = info_from_operation
        self.info_to_operation = info_to_operation
        self.amount_operation = amount_operation
        self.currency_operation = currency_operation

    def __repr__(self):

        """Для отладки: выводит операцию и её свойства"""

        return f'{self.__class__.__name__}(' \
               f'data="{self.data_operation}", ' \
               f'description={self.description_operation}, ' \
               f'info_from="{self.info_from_operation}" ' \
               f'info_to="{self.info_to_operation}" ' \
               f'amount="{self.amount_operation}" ' \
               f'currency="{self.currency_operation}" ' \
               f')'
