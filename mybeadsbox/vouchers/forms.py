from django.forms import ModelForm

from vouchers.models import VoucherTemplate, Voucher


class VoucherTemplateForm(ModelForm):
    class Meta:
        model = VoucherTemplate
        fields = ("title", "description", "price", "currency")


class VoucherPurchaseForm(ModelForm):
    class Meta:
        model = Voucher
        fields = ("buyer",)
