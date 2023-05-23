# Generated by Django 4.2.1 on 2023-05-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_id', models.CharField(max_length=10)),
                ('c_employee_name', models.CharField(max_length=40)),
                ('c_premises_id', models.CharField(max_length=10)),
                ('c_supplier_company_name', models.CharField(max_length=40)),
                ('start_date', models.DateField()),
                ('accounting_date', models.DateField()),
                ('amortisation_period', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=30)),
                ('cpu', models.CharField(max_length=250)),
                ('gpu', models.CharField(max_length=250)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Premises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premises_id', models.CharField(max_length=3)),
                ('p_section_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=10)),
                ('section_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_id', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('inn', models.CharField(max_length=10)),
            ],
        ),
    ]