import re


def get_mask_account(from_or_to_account):
    """ Возвращает замаскированный номер счёта """
    str_digit = re.sub(r'\D', '', from_or_to_account)
    str_alpha = re.sub(r'\d+', '', from_or_to_account)
    mask_digits = (len(str_digit) - 4) * '*'
    return f'{str_alpha}{mask_digits}{from_or_to_account[-4:]}'


def get_mask_card(from_or_to_card):
    """ Возвращает замаскированный номер карты """
    last_four_digit = 4 * '*'
    first_six_digit = 6 * '*'
    str_digit = re.sub(r'\D', '', from_or_to_card)
    str_alpha = re.sub(r'\d+', '', from_or_to_card)
    mask_digit = first_six_digit + str_digit[7:-3] + last_four_digit
    masked_number = ' '.join([mask_digit[i:i + 4] for i in range(0, len(mask_digit), 4)])
    return f'{str_alpha}{masked_number}'
