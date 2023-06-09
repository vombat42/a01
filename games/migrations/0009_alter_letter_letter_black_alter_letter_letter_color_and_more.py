# Generated by Django 4.2.1 on 2023-05-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_alter_letter_letter_black_alter_letter_letter_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='letter_black',
            field=models.ImageField(blank=True, null=True, upload_to='games/img/black/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_color',
            field=models.ImageField(blank=True, null=True, upload_to='games/img/color/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_outline',
            field=models.ImageField(blank=True, null=True, upload_to='games/img/outline/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='voice',
            field=models.FileField(upload_to='games/voice'),
        ),
        migrations.AlterField(
            model_name='word',
            name='voice',
            field=models.FileField(upload_to='games/voice'),
        ),
    ]
