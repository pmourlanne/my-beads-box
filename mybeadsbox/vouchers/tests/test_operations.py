import pytest

from vouchers.operations import _is_voucher_status_transition_valid


@pytest.mark.parametrize(
    "status, new_status, authorized",
    [
        ("purchased", "purchased", False),
        ("purchased", "cancelled", True),
        ("purchased", "used", True),
        ("purchased", "expired", True),
        ("used", "expired", False),
        ("cancelled", "refunded", True),
    ],
)
def test_is_voucher_status_transition_valid(status, new_status, authorized):
    assert _is_voucher_status_transition_valid(status, new_status) is authorized
