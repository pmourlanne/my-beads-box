import pytest

from vouchers.models import Voucher


@pytest.mark.parametrize("status, new_status, authorized", [
    ("purchased", "purchased", False),
    ("purchased", "cancelled", True),
    ("purchased", "used", True),
    ("purchased", "expired", True),
    ("used", "expired", False),
])
def test_is_voucher_status_transition_valid(status, new_status, authorized):
    voucher = Voucher(status=status)
    assert voucher.is_new_status_valid(new_status) is authorized
