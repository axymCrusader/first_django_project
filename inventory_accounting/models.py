from django.db import models


class Supplier(models.Model):
    supplier_id = models.CharField(max_length=10)
    company_name = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    inn = models.CharField(max_length=10)

    def __str__(self):
        return self.supplier_id


class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.employee_id


class Premises(models.Model):
    premises_id = models.CharField(max_length=3)
    p_section_name = models.CharField(max_length=50) # тут должен быть внешний ключ

    def __str__(self):
        return self.premises_id


class Computer(models.Model):
    computer_id = models.CharField(max_length=10)
    c_employee_name = models.CharField(max_length=40) # тут должен быть внешний ключ 
    c_premises_id = models.CharField(max_length=10) # тут должен быть внешний ключ
    c_supplier_company_name = models.CharField(max_length=40) # тут должен быть внешний ключ
    start_date = models.DateField(auto_now=False)
    accounting_date = models.DateField(auto_now=False)
    amortisation_period = models.IntegerField()
    manufacturer = models.CharField(max_length=30)
    cpu = models.CharField(max_length=250)
    gpu = models.CharField(max_length=250)
    ram = models.IntegerField()
    rom = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.computer_id


class Section(models.Model):
    section_id = models.CharField(max_length=10)
    section_name = models.CharField(max_length=250)

    def __str__(self):
        return self.section_id