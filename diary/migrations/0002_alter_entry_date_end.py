# Generated by Django 4.1.7 on 2023-04-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_end',
            field=models.DateTimeField(blank=True),
        ),
    ]
