# Generated by Django 4.1.7 on 2023-04-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_alter_bot_height_alter_bot_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='birthday',
            field=models.DateField(),
        ),
    ]
