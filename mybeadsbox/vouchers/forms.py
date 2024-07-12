from django.forms import ModelForm

from vouchers.models import VoucherTemplate

class VoucherTemplateForm(ModelForm):
    class Meta:
        model = VoucherTemplate
        fields = ("title", "description", "price", "currency")
