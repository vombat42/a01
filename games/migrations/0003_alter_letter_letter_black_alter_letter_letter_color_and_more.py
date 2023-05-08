# Generated by Django 4.1.7 on 2023-05-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_letter_letter_black_alter_letter_letter_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='letter_black',
            field=models.ImageField(upload_to='games/static/img/black/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_color',
            field=models.ImageField(upload_to='games/static/img/color/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_outline',
            field=models.ImageField(upload_to='games/static/img/outline/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='voice',
            field=models.FileField(upload_to='games/static/voice'),
        ),
        migrations.AlterField(
            model_name='word',
            name='voice',
            field=models.FileField(upload_to='games/static/voice'),
        ),
    ]
