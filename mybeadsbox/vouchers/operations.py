from vouchers.models import Voucher


VOUCHER_STATUS_TRANSITIONS = {
    "purchased": ("cancelled", "used", "expired"),
    "cancelled": ("refunded",),
    "refunded": (),
    "used": (),
    "expired": (),
}


def create_voucher(*, template, buyer):
    """
    Create a voucher from a template for a particular buyer

    We denormalize the data from the template, since the template may change
    and we don't want the data on the voucher to change over time (in particular the price!)
    """
    template_values = {
        key: getattr(template, key)
        for key in ["title", "description", "price", "currency"]
    }

    return Voucher.objects.create(
        buyer=buyer, status="purchased", template=template, **template_values
    )


def _is_voucher_status_transition_valid(status, new_status):
    return new_status in VOUCHER_STATUS_TRANSITIONS[status]


class UnexpectedVoucherStatusChange(Exception):
    pass


def update_voucher_status(*, voucher, status):
    """
    Update the status of a voucher, saves the change and returns the voucher
    Raises an UnexpectedVoucherStatusChange if change is not valid

    NB: This doesn't handle race conditions, use at your own risk
    """
    if not _is_voucher_status_transition_valid(voucher.status, status):
        raise UnexpectedVoucherStatusChange(
            f"Voucher cannot go from {voucher.status} to {status}"
        )

    voucher.status = status
    voucher.save()

    return voucher
