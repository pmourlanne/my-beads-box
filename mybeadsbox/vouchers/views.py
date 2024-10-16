from django.forms import modelform_factory
from django.shortcuts import redirect, render, get_object_or_404

from vouchers.forms import VoucherTemplateForm, VoucherPurchaseForm
from vouchers.models import VoucherTemplate, Voucher
from vouchers.operations import (
    create_voucher,
    update_voucher_status,
    UnexpectedVoucherStatusChange,
)


def list_templates(request):
    return render(
        request, "templates.html", {"templates": VoucherTemplate.objects.all()}
    )


def create_template(request):
    if request.method == "POST":
        form = VoucherTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin-list-templates")
    else:
        form = VoucherTemplateForm()

    return render(request, "create_template.html", {"form": form})


def edit_template(request, template_id):
    template = get_object_or_404(VoucherTemplate, id=template_id)

    if request.method == "POST":
        form = VoucherTemplateForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
            return redirect("admin-list-templates")
    else:
        form = VoucherTemplateForm(instance=template)

    return render(request, "edit_template.html", {"form": form, "template": template})


def list_vouchers(request):
    return render(
        request, "vouchers.html", {"templates": VoucherTemplate.objects.all()}
    )


def purchase_voucher(request):
    template_id = request.GET.get("template_id")
    template = get_object_or_404(VoucherTemplate, id=template_id)

    if request.method == "POST":
        form = VoucherPurchaseForm(request.POST)
        if form.is_valid():
            # TODO: Stripe
            create_voucher(template=template, buyer=form.cleaned_data["buyer"])
            return redirect("list-vouchers")

    else:
        form = VoucherPurchaseForm()

    return render(
        request, "purchase_voucher.html", {"form": form, "template": template}
    )


def admin_list_vouchers(request):
    return render(
        request,
        "admin_vouchers.html",
        {"vouchers": Voucher.objects.all().select_related("template")},
    )


def admin_update_voucher_status(request, voucher_id):
    voucher = get_object_or_404(Voucher, id=voucher_id)

    if request.method == "POST":
        form = modelform_factory(Voucher, fields=("status",))(request.POST)
        if form.is_valid():
            try:
                update_voucher_status(
                    voucher=voucher, status=form.cleaned_data.get("status")
                )
            except UnexpectedVoucherStatusChange:
                # Probably want to log something :clown:
                pass

    return redirect("admin-list-vouchers")
