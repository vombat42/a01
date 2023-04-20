# Generated by Django 4.1.7 on 2023-04-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowhow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
