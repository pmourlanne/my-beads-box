from vouchers.views import list_templates, create_template, edit_template, list_vouchers, purchase_voucher, admin_list_vouchers, admin_update_voucher_status
from django.urls import path

urlpatterns = [
    path("admin/templates/", list_templates, name='admin-list-templates'),
    path("admin/templates/create", create_template, name='create-template'),
    path("admin/templates/<uuid:template_id>", edit_template, name='edit-template'),
    path("admin/vouchers/", admin_list_vouchers, name='admin-list-vouchers'),
    path("admin/voucher/<uuid:voucher_id>/status", admin_update_voucher_status, name='admin-update-voucher-status'),
    path("", list_vouchers, name='list-vouchers'),
    path("purchase/", purchase_voucher, name='purchase-voucher'),
]
