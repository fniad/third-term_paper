class Operation:

    """Класс операции"""

    def __init__(self, data_operation, info_operation, info_from_operation, info_to_operation):

        """Устанавливает необходимые атрибуты операции"""

        self.data_operation = data_operation
        self.info_operation = info_operation
        self.info_from_operation = info_from_operation
        self.info_to_operation = info_to_operation

        self.amount_operation = '0.00'
        self.currency_operation = 'руб.'

    def __repr__(self):

        """Для отладки: выводит операцию и её свойства"""

        return f'{self.__class__.__name__}(' \
               f'data_operation="{self.data_operation}", ' \
               f'dinfo_operation={self.info_operation}, ' \
               f'info_from_operation="{self.info_from_operation}" ' \
               f'info_in_to_operation="{self.info_to_operation}" ' \
               f')'
