# Generated by Django 4.2.1 on 2023-05-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premises',
            name='p_section_name',
            field=models.CharField(max_length=50),
        ),
    ]
