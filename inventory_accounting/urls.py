"""
URL configuration for accounting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from inventory_accounting import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add', views.add, name='add'),

    path('edit', views.edit, name='edit'),

    path('report', views.report, name='report'),

    path('form_add_section', views.form_add_section, name='form_add_section'),

    path('add_section', views.add_section, name='add_section'),

    path('form_add_employee', views.form_add_employee, name='form_add_employee'),

    path('add_employee', views.add_employee, name='add_employee'),

    path('form_add_premises', views.form_add_premises, name='form_add_premises'),

    path('add_premises', views.add_premises, name='add_premises'),

    path('form_add_supplier', views.form_add_supplier, name='form_add_supplier'),

    path('add_supplier', views.add_supplier, name='add_supplier'),

    path('form_add_computer', views.form_add_computer, name='form_add_computer'),

    path('add_computer', views.add_computer, name='add_computer'),

    path('edit_employee', views.edit_employee, name='edit_employee'),

    path('edit_computer', views.edit_computer, name='edit_computer'),

    path('edit_premises', views.edit_premises, name='edit_premises'),

    path('edit_section', views.edit_section, name='edit_section'),

    path('edit_supplier', views.edit_supplier, name='edit_supplier'),

    path("delete_employee/<int:id>/", views.delete_employee),

    path("delete_supplier/<int:id>/", views.delete_supplier),

    path("delete_section/<int:id>/", views.delete_section),

    path("delete_premises/<int:id>/", views.delete_premises),

    path("delete_computer/<int:id>/", views.delete_computer),

    path('form_edit_employee/<int:id>/', views.form_edit_employee),

    path('form_edit_section/<int:id>/', views.form_edit_section),

    path('form_edit_supplier/<int:id>/', views.form_edit_supplier),

    path('form_edit_premises/<int:id>/', views.form_edit_premises),

    path('form_edit_computer/<int:id>/', views.form_edit_computer),

    path('date_export_xls', views.date_export_xls, name='date_export_xls'),

    path('employee_export_xls', views.employee_export_xls, name='employee_export_xls')
]
