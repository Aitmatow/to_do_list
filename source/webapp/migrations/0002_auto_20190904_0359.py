# Generated by Django 2.2.4 on 2019-09-04 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='done_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата выполнения'),
        ),
    ]
