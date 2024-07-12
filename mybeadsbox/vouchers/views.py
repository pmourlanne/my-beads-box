from django.shortcuts import redirect, render, get_object_or_404

from vouchers.forms import VoucherTemplateForm
from vouchers.models import VoucherTemplate


def list_templates(request):
    context = {
        "templates": VoucherTemplate.objects.all(),
    }
    return render(request, "templates.html", context)


def create_template(request):
    if request.method == "POST":
        form = VoucherTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-templates")
    else:
        form = VoucherTemplateForm()

    return render(request, "create_template.html", {"form": form})


def edit_template(request, template_id):
    template = get_object_or_404(VoucherTemplate, id=template_id)

    if request.method == "POST":
        form = VoucherTemplateForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
            return redirect("list-templates")
    else:
        form = VoucherTemplateForm(instance=template)

    return render(request, "edit_template.html", {"form": form, "template": template})

