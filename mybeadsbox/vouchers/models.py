import uuid

from django.db import models

from vouchers.utils import get_price_display


CURRENCIES = (
    ("EUR", "€"),
    ("USD", "$"),
)


STATUSES = (
    ("purchased", "Purchased"),
    ("cancelled", "Cancelled"),
    ("used", "Used"),
    ("expired", "Expired"),
)


class VoucherTemplate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField(help_text="In minor units")  # In minor units
    currency = models.CharField(max_length=None, choices=CURRENCIES)

    # TODO: metadata (created, modified?)

    def get_price_display(self):
        return get_price_display(self.price, self.currency)


class Voucher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # TODO: What if the template changes? -> Denormalize / django-simple-history
    template = models.ForeignKey(VoucherTemplate, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=100)  # In reality will probably be a FK to a User
    status = models.CharField(max_length=None, choices=STATUSES)

    # TODO: metadata (created, modified?)
