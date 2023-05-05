from utils.utils_mask import get_mask_account, get_mask_card


def test_get_mask_card():
    assert get_mask_card("Visa 1524025455441624") == "Visa **** **54 5544 ****"
    assert get_mask_card("Visa Platinum 8990922113665229") == "Visa Platinum **** **21 1366 ****"
    assert get_mask_card("Maestro 8990922113665229") == "Maestro **** **21 1366 ****"
    assert get_mask_card("МИР 1524025455441624") == "МИР **** **54 5544 ****"


def test_get_mask_account():
    assert get_mask_account("Счет 44238164562083919420") == "Счет ****************9420"
