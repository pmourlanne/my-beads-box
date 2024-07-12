from vouchers.views import list_templates, create_template, edit_template
from django.urls import path

urlpatterns = [
    path("templates/", list_templates, name='list-templates'),
    path("templates/create", create_template, name='create-template'),
    path("templates/<uuid:template_id>", edit_template, name='edit-template'),
]
