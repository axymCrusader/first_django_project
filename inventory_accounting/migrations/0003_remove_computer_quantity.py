# Generated by Django 4.2.1 on 2023-05-23 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_accounting', '0002_alter_premises_p_section_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='quantity',
        ),
    ]
