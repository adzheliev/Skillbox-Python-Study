# Generated by Django 4.1.6 on 2023-02-21 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_order_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descount',
            new_name='discount',
        ),
    ]