import pytest
from data.operations import Operation
from utils.utils_mask import get_mask_account, get_mask_card


@pytest.fixture
def operation_1():
    return Operation('2018-07-31T12:25:32.579413',
                     'Перевод с карты на счет',
                     'Visa Gold 6527183396477720',
                     'Счет 38573816654581789611',
                     '77302.31',
                     'USD')


@pytest.fixture
def operation_2():
    return Operation('2019-04-11T23:10:21.514616',
                     'Перевод с карты на карту',
                     'МИР 8193813157568899',
                     'МИР 9425591958944146',
                     '2621.51',
                     'руб.')


@pytest.fixture
def operation_3():
    return Operation('2019-06-14T19:37:49.044089',
                     'Перевод со счета на счет',
                     'Счет 73222753239048295679',
                     'Счет 78544755774551298747',
                     '2621.51',
                     'USD')


@pytest.fixture
def operation_4():
    return Operation('2019-06-14T19:37:49.044089',
                     'Перевод со счета на карту',
                     None,
                     'Maestro 7810846596785568',
                     '2621.51',
                     'USD')


def test_get_normal_format_data(operation_1, operation_2, operation_4):
    assert operation_1.get_normal_format_data() == '31.07.2018'
    assert operation_2.get_normal_format_data() == '11.04.2019'
    assert operation_4.get_normal_format_data() == '14.06.2019'


def test_get_type_from(operation_1, operation_2, operation_3, operation_4):
    assert operation_1.get_type_from() == get_mask_card('Visa Gold 6527183396477720')
    assert operation_2.get_type_from() == get_mask_card('МИР 8193813157568899')
    assert operation_3.get_type_from() == get_mask_account('Счет 73222753239048295679')
    assert operation_4.get_type_from() == 'Неизвестно'


def test_get_type_to(operation_1, operation_2, operation_4):
    assert operation_1.get_type_to() == get_mask_account('Счет 38573816654581789611')
    assert operation_2.get_type_to() == get_mask_card('МИР 9425591958944146')
    assert operation_4.get_type_to() == get_mask_card('Maestro 7810846596785568')


def test_get_result_operation(operation_1, operation_4):
    assert operation_1.get_result_operation() == f'{operation_1.get_normal_format_data()} {operation_1.description_operation} \n' \
                                                 f'{operation_1.get_type_from()} -> {operation_1.get_type_to()} \n' \
                                                 f'{operation_1.amount_operation} {operation_1.currency_operation}'
    assert operation_4.get_result_operation() == f'{operation_4.get_normal_format_data()} {operation_4.description_operation} \n' \
                                                 f'{operation_4.get_type_from()} -> {operation_4.get_type_to()} \n' \
                                                 f'{operation_4.amount_operation} {operation_4.currency_operation}'
