# Generated by Django 3.0.6 on 2020-06-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200604_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('На доставке', 'На доставке'), ('Уже доставлен', 'Уже доставлен')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('На складе', 'На складе'), ('Не на складе', 'Не на складе')], max_length=200, null=True),
        ),
    ]
