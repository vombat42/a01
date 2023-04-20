# Generated by Django 4.1.7 on 2023-04-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_entry_date_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='links',
            field=models.ManyToManyField(blank=True, null=True, to='diary.link'),
        ),
    ]
