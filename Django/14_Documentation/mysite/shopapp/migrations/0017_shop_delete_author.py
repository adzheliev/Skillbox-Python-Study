# Generated by Django 4.1.6 on 2023-04-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0016_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
