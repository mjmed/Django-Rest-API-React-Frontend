# Generated by Django 2.1.15 on 2020-06-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anestesias', '0003_auto_20200601_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anestesia',
            name='dia_cirugia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='anestesia',
            name='tipo_cirugia',
            field=models.CharField(max_length=200),
        ),
    ]
