import pytest

from vouchers.utils import get_price_display


@pytest.mark.parametrize(
    "amount, currency, expected",
    [
        (1234, "EUR", "12.34€"),
        (9876, "USD", "$98.76"),
        (9876, "CAD", None),
    ],
)
def test_get_price_display(amount, currency, expected):
    if expected:
        assert get_price_display(amount, currency) == expected
    else:
        with pytest.raises(ValueError):
            get_price_display(amount, currency)
